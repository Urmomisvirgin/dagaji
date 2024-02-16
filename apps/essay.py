import logging
import os
from datetime import datetime

import pyperclip

from prompt_templates import productivity
from tools import helpers, llm

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

selected_model = "gpt-4-1106-preview"


def expand_content():
    """
    Fetch content from clipboard and expand it into an essay with a title using the LLM model.
    Returns a tuple of (title, essay_content).
    """
    try:
        content = pyperclip.paste()
        prompt = productivity.write_essay_like_Joe.format(user_input=content)

        # Get the response as a string from the LLM
        response_text = llm.llm_generate_text_with_save(
            prompt, "OpenAI", selected_model
        )

        # Process the response text to extract title and essay content
        lines = response_text.strip().split("\n")
        title = lines[0] if len(lines) > 0 else "Untitled Essay"
        essay_content = "\n".join(lines[1:])
        return title, essay_content
    except Exception as e:
        logging.error(f"Error in content expansion: {e}")
        raise


def create_markdown_file(title, content, vault_path):
    """
    Create a markdown file with the given title and content in the specified vault path.
    Returns the file path of the created file.
    """
    try:
        if not os.path.exists(vault_path):
            os.makedirs(vault_path)

        # Sanitize the title to create a valid file name
        file_name = (
            "".join(char for char in title if char.isalnum() or char in " _-").rstrip()
            + ".md"
        )
        file_path = os.path.join(vault_path, file_name)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_path, "w") as file:
            file.write(f"📝 {title}\n\n")
            file.write(f"⏳ Created Time: {current_time}\n\n")
            file.write(f"🏷️ Tags: #essay \n\n")
            file.write(content)
            file.write("\n\n## Additional Notes\n\n")
        return file_path
    except Exception as e:
        logging.error(f"Error in file creation: {e}")
        raise


def main(vault_path):
    """
    Main function to expand content from clipboard and create a markdown file in the specified vault.
    """
    try:
        title, expanded_essay = expand_content()
        file_path = create_markdown_file(title, expanded_essay, vault_path)
        logging.info(f"✅ File: [{title}] created at {file_path}")
        print("--------------------------------------")
        print(expanded_essay)
    except Exception as e:
        logging.error(f"❌ ", e)


if __name__ == "__main__":
    # Example Vault Path
    vault_path = "/Users/btxz./Desktop/BIOCHEM degree/"
    main(vault_path)
