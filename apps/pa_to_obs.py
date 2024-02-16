import sys
from datetime import datetime

import PyPDF2

sys.path.append("/Users/btxz./Documents/GitHub/dagaji/")
from prompt_templates import productivity
from tools import helpers, llm


def read_pdf(file_path):
    """
    Reads a PDF file and extracts the text content using the updated PdfReader.
    """
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)  # Updated to PdfReader
        text_content = ""
        for page in pdf_reader.pages:
            text_content += page.extract_text()  # Updated method name
    return text_content


def remove_references(text):
    """
    Removes the references section from the research paper text.
    """
    # Common headings for references section in research papers
    reference_headings = ["References", "Bibliography", "Works Cited"]
    for heading in reference_headings:
        if heading in text:
            text = text.split(heading)[0]
            break
    return text


def process_text_content(text, model):
    """
    Processes the input text by dividing it into chunks and summarizing each chunk.
    """
    # First, remove references to manage token limits
    text_without_references = remove_references(text)

    # Check if text is too long and needs to be split into chunks
    if (
        helpers.count_tokens(text_without_references, model)
        > helpers.max_tokens_per_chunk
    ):
        chunks = helpers.split_text_into_chunks(
            text_without_references, helpers.max_tokens_per_chunk
        )
    else:
        chunks = [text_without_references]

    overall_output = ""
    input_token_count = helpers.count_tokens(
        text_without_references, model
    )  # Count input tokens here

    for chunk in chunks:
        prompt = productivity.best_research_paper_summary.format(user_input=chunk)
        try:
            chunk_response = llm.llm_generate_text_with_save(prompt, "OpenAI", model)
            overall_output += chunk_response
        except Exception as e:
            print(f"Error processing chunk: {e}")
            continue

    output_token_count = helpers.count_tokens(
        overall_output, model
    )  # Count output tokens here

    return overall_output, input_token_count, output_token_count


def create_obsidian_file(title: str, content: str):
    """
    Creates a new markdown file in the Obsidian vault with the given title, content,
    and includes the current timestamp.
    """
    safe_title = title.replace("/", "-").replace("\\", "-")
    filepath = f"/Users/btxz./Desktop/BIOCHEM degree/{safe_title}.md"

    # Get current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "w") as file:
        file.write("🔖 Tags: #NNS #metabolic_health #dissertation \n\n")
        file.write(f"🕒 Created: {current_time}\n\n")  # Add timestamp here
        file.write("---\n\n")
        file.write(format_summary(content))


def format_summary(summary: str) -> str:
    return summary


if __name__ == "__main__":

    selected_model = "gpt-4-1106-preview"

    if len(sys.argv) == 3:
        pdf_file_path = sys.argv[1]
        obsidian_title = sys.argv[2]

        try:
            research_content = read_pdf(pdf_file_path)
            summarized_output, input_token_count, output_token_count = (
                process_text_content(research_content, selected_model)
            )

            if summarized_output:
                create_obsidian_file(obsidian_title, summarized_output)
                print("✅ File Created Successfully")
                # Print the token counts and any other relevant information here if needed
                print(
                    f"Input Tokens: {input_token_count}, Output Tokens: {output_token_count}"
                )
                print("--------------------------------------")
                print(summarized_output)

            else:
                print("❌ Failed to generate a summary.")
        except Exception as e:
            print(f"Error reading PDF file: {e}")
    else:
        print(
            "Please provide the path to a PDF file and a title for the Obsidian file as arguments."
        )
