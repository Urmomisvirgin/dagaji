from functions import helpers, llm
from prompt_templates import youtube, twitter

selected_model = "gpt-3.5-turbo"

youtube_url = ""

video_transcript = helpers.get_video_transcript(youtube_url)

prompt = youtube.tweet_from_youtube_prompt.format(transcript = video_transcript)

response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)

print("Joe's Slave 💩: \n", response)