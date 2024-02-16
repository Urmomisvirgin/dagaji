import sys 
sys.path.append('/Users/btxz./Documents/GitHub/dagaji/')
from tools import helpers, llm
from datetime import datetime
from prompt_templates import productivity
import requests
from bs4 import BeautifulSoup

def get_youtube_title(url):
    # Send a request to the YouTube URL and parse the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title from the HTML
    return soup.find('title').text

def process_video_transcript(url, model):
    # Retrieve video transcript
    video_transcript = helpers.get_video_transcript(url)

    # Initialize token counts
    input_token_count = 0
    output_token_count = 0

    # Count tokens for the video transcript
    if helpers.count_tokens(video_transcript, model) > helpers.max_tokens_per_chunk:
        chunks = helpers.split_text_into_chunks(video_transcript, helpers.max_tokens_per_chunk)
    else:
        chunks = [video_transcript]

    overall_output = ""
    # Process each chunk to summarize
    for chunk in chunks:
        input_token_count += helpers.count_tokens(chunk, model)  # Corrected function call
        prompt = productivity.wisdom_extraction.format(user_input=chunk)
        try:
            # Generate summary for each chunk using the language model
            chunk_response = llm.llm_generate_text_with_save(prompt, "OpenAI", model)
            overall_output += chunk_response
            output_token_count += helpers.count_tokens(chunk_response, model)  # Corrected function call
        except Exception as e:
    # Convert the exception to a string before concatenating
            print(f"Error processing chunk: {str(e)}")
            continue


    return overall_output, input_token_count, output_token_count

def create_obsidian_file(title: str, content: str, url: str):
    # Replace characters in title that are not allowed in file names
    safe_title = str(title).replace('/', '-').replace('\\', '-')

    # Define the file path for the new Obsidian file
    filepath = f"/Users/btxz./Desktop/BIOCHEM degree/{safe_title}.md"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write the content in markdown format to the file
    with open(filepath, 'w') as file:
        file.write(f"[🌐 {title}]({url})\n\n")
        file.write(f"🔖 Tags: #youtube #wisdom #podcast \n\n")
        file.write(f"🕒 Created: {current_time}\n\n")  # Add timestamp here
        file.write("---\n\n")  # Horizontal line for visual separation
        file.write("## 📝 Summary\n\n")
        file.write(format_summary(content))  # Add the formatted summary

def format_summary(summary: str) -> str:
    # Split the summary into sections based on the headers (like '# ONE SENTENCE SUMMARY:')
    sections = summary.split('- # ')
    formatted_summary = ""

    for section in sections:
        if section.strip():
            # Split the section into lines
            lines = section.split('\n')
            # Add the header back with Markdown formatting
            formatted_summary += f"### {lines[0].strip()}\n\n"
            # Add the remaining lines
            for line in lines[1:]:
                if line.strip():
                    formatted_summary += f"{line.strip()}\n\n"
            # Add a horizontal line for separation between sections
            formatted_summary += "---\n\n"

    return formatted_summary.strip()

# Main Execution
if __name__ == "__main__":
    selected_model = "gpt-4-1106-preview"

    # Check if a YouTube URL is provided as a command line argument
    if len(sys.argv) > 1:
        youtube_url = sys.argv[1]
        video_title = get_youtube_title(youtube_url)
        summarized_output, input_tokens, output_tokens = process_video_transcript(youtube_url, selected_model)
        print(summarized_output)

        if summarized_output:
            create_obsidian_file(video_title, summarized_output, youtube_url)
            print("✅ File Created Successfully")

            # Calculate and print the cost
            total_cost = helpers.estimate_total_cost(selected_model, input_tokens, output_tokens)
            print(f"💰 Cost: ${total_cost:.4f}")
            print("--------------------------------------")
        else:
            print("❌ Failed to generate a summary.")
    else:
        print("Please provide a YouTube URL as an argument.")
