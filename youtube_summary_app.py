# Import necessary libraries
import streamlit as st
from functions import helpers, llm
from prompt_templates import youtube

# The main function where we will build our page
def main():
    # Streamlit page configurations
    st.set_page_config(page_title="Video Transcript Summarizer", layout="wide")

    # Title of the web app
    st.title("Video Transcript Summarizer")

    # Sidebar for user inputs
    st.sidebar.header("User Input Options")

    # Input for the YouTube URL
    youtube_url = st.sidebar.text_input("Enter YouTube Video URL", "https://www.youtube.com/watch?v=0zi-CG_iB6w")

    # Button to start processing
    process_button = st.sidebar.button("Process Video")

    # Check if the button is pressed
    if process_button:
        # Display a message while processing
        with st.spinner("Processing..."):
            # Fetch the video transcript using the helper function
            video_transcript = helpers.get_video_transcript(youtube_url)

            # Split transcript into chunks if necessary
            if helpers.count_tokens(video_transcript, "gpt-3.5-turbo") > helpers.max_tokens_per_chunk:
                chunks = helpers.split_text_into_chunks(video_transcript, helpers.max_tokens_per_chunk)
            else:
                chunks = [video_transcript]

            # Initialize overall output
            overall_output = ""

            # Process each chunk
            for chunk in chunks:
                # Prepare the prompt for summarization
                prompt = youtube.youtube_to_points_summary.format(transcript=chunk)
                # Get the response from the language model
                chunk_response = llm.llm_generate_text_with_save(prompt, "OpenAI", "gpt-3.5-turbo")
                # Append the response to overall output
                overall_output += chunk_response

            # Display the final summarized output
            st.subheader("Summary")
            st.write(overall_output)

# Running the main function
if __name__ == "__main__":
    main()
