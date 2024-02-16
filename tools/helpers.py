import tiktoken
import openai
import newspaper
import re
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import TokenTextSplitter


openai.api_key = "sk-mLBpYLAxHWpHLc1aD7DdFcE76f39415a9aE7691171147021"


# def count_tokens(text, selected_model):
#     encoding = tiktoken.encoding_for_model(selected_model)
#     num_tokens = encoding.encode(text)
#     return len(num_tokens)

# def estimate_input_cost(model_name, token_count):
#     model_costs = {
#         "gpt-3.5-turbo": 0.0015,
#         "gpt-3.5-turbo-16k": 0.003,
#         "gpt-4": 0.03,
#         "gpt-4-32k": 0.06,
#         "gpt-4-1106-preview": 0.01,
#     }

#     cost_per_1000_tokens = model_costs.get(model_name, 0)  # Default cost is 0 if model not found
#     estimated_cost = (token_count / 1000) * cost_per_1000_tokens
#     return estimated_cost

def count_tokens(text, selected_model):
    encoding = tiktoken.encoding_for_model(selected_model)
    
    # Count tokens for the text
    tokens = encoding.encode(text)
    token_count = len(tokens)

    return token_count

def estimate_total_cost(model_name, input_token_count, output_token_count):
    # Define the cost per token for input for each model
    input_model_costs = {
        "gpt-3.5-turbo": 0.003/1000,
        "gpt-3.5-turbo-1106": 0.001/1000,
        "gpt-4-1106-preview": 0.01/1000,
        "gpt-4": 0.03/1000,
        "gpt-4-32k": 0.06/1000,
    }

    # Define the cost per token for output for each model
    output_model_costs = {
        "gpt-3.5-turbo": 0.006/1000,
        "gpt-3.5-turbo-1106	": 0.002/1000,
        "gpt-4-1106-preview": 0.03/1000,
        "gpt-4": 0.06/1000,
        "gpt-4-32k": 0.12/1000,
    }

    # Check if the model name is in the dictionaries
    if model_name not in input_model_costs or model_name not in output_model_costs:
        raise ValueError("Unknown model name.")

    # Calculate the total cost
    input_cost_per_token = input_model_costs[model_name]
    output_cost_per_token = output_model_costs[model_name]
    total_cost = (input_token_count * input_cost_per_token) + (output_token_count * output_cost_per_token)

    return total_cost

def ask_ai(user_prompt):
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # you can replace this with your preferred model
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": user_prompt}
                  ],
    )
    return completion.choices[0].message.content


def get_article_from_url(url):
    try: 
        #scrape the web page for content using newspaper 
        article = newspaper.Article(url)
        #download the article's content with a timeout of 10 seconds 
        article.download()
        # Check if the download was successful before parsing the article 
        if article.download_state == 2:
            article.parse()
            #Get the main text content of the article
            article_text = article.text 
            return article_text 
        else: 
            print("Error: Unable to download article from URL:", url)
    except Exception as e:
        print("An error occurred while processing the URL:", url)
        print(str(e))
        return None


def get_video_transcript(video_url):
    match = re.search(r"(?:youtube\.com\/watch\?v=|youtu\.be\/)(.*)", video_url)
    if match:
        VIDEO_ID = match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")

    video_id = VIDEO_ID

    # Fetch the transcript using the YouTubeTranscriptApi
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Extract the text of the transcript
    transcript_text = ""
    for line in transcript:
        transcript_text += line["text"] + " "
    return transcript_text
    
    
def split_text_into_chunks(text, max_tokens):
    text_splitter = TokenTextSplitter(chunk_size=max_tokens, chunk_overlap=0)
    chunks = text_splitter.split_text(text)
    return chunks

max_tokens_per_chunk = 50000

















