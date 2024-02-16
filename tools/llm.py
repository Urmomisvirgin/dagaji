import json

import cohere
import nlpcloud
import openai
import requests
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

"""
LLMs:
OpenAI
NlpCloud
Cohere
You can add your own
"""


# def llm_generate_text(prompt,service,model):
#     if service == 'OpenAI':
#         generated_text = openai_generate(prompt,model)
#     elif service == 'NlpCloud':
#         generated_text = nlp_cloud_generate(prompt,model)
#     elif service == 'Cohere':
#         generated_text = cohere_generate(prompt,model)

#     return generated_text


def llm_generate_text_with_save(prompt, service, model):
    if service == "OpenAI":
        generated_text = openai_generate(prompt, model)
        # save generated text
    elif service == "NlpCloud":
        generated_text = nlp_cloud_generate(prompt, model)
    elif service == "Cohere":
        generated_text = cohere_generate(prompt, model)

    save_to_json(prompt, generated_text)
    return generated_text


# Open AI Function
openai.api_key = "sk-mLBpYLAxHWpHLc1aD7DdFcE76f39415a9aE7691171147021"

# New API URL
API_URL = "https://kapkey.chatgptapi.org.cn/v1"


def openai_generate(user_prompt, selected_model):
    # Data for the request
    data = {
        "model": selected_model,
        "messages": [{"role": "user", "content": user_prompt}],
        "max_tokens": 4000,
    }

    # Make the POST request
    response = requests.post(
        f"{API_URL}/chat/completions",
        headers={
            "Authorization": "Bearer sk-mLBpYLAxHWpHLc1aD7DdFcE76f39415a9aE7691171147021",
            "Content-Type": "application/json",
        },
        data=json.dumps(data),
    )

    # Check the response
    if response.status_code == 200:
        response_data = response.json()
        generated_text = response_data["choices"][0]["message"]["content"]
        return generated_text
    else:
        # Return an error message in case of a problem
        return f"Error: {response.status_code}, {response.text}", None


# def openai_generate(user_prompt,selected_model):
#     completion = openai.chat.completions.create(
#         model=selected_model,
#         messages=[
#             {"role": "user", "content": user_prompt}
#         ],
#         max_tokens= 6000,
#     )
#     return completion.choices[0].message.content


# nlpCloud Function
nlp_cloud_key = "f1720b3bc2102ddf9"


def nlp_cloud_generate(user_prompt, selected_model):
    client = nlpcloud.Client(selected_model, nlp_cloud_key, gpu=True, lang="en")
    result = client.generation(
        user_prompt,
        min_length=0,
        max_length=100,
        length_no_input=True,
        remove_input=True,
        end_sequence=None,
        top_p=1,
        temperature=0.8,
        top_k=50,
        repetition_penalty=1,
        length_penalty=1,
        do_sample=True,
        early_stopping=False,
        num_beams=1,
        no_repeat_ngram_size=0,
        num_return_sequences=1,
        bad_words=None,
        remove_end_sequence=False,
    )
    return result["generated_text"]


# Cohere API
cohere_api_key = "fk8B74dEf1DlsdzIGkA4lL"


def cohere_generate(user_prompt, selected_model):
    co = cohere.Client(cohere_api_key)  # This is your trial API key
    response = co.generate(
        model=selected_model,
        prompt=user_prompt,
        max_tokens=300,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods="NONE",
    )

    return response.generations[0].text


def save_to_json(prompt, response):
    data = {"prompt": prompt, "response": response}
    with open("ai_prompt_responses.json", "a") as f:
        f.write(json.dumps(data) + "\n")
