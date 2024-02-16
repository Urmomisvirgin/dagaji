import requests
import json
import sseclient

API_URL = 'https://kapkey.chatgptapi.org.cn/v1'
API_key = "sk-mLBpYLAxHWpHLc1aD7DdFcE76f39415a9aE7691171147021"
prompt = "write a poem about california sunrise"

def request_with_stream(user_prompt):
    headers = {
        "Authorization": f"Bearer {API_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": 'text-davinci-003',
        "messages": [{"role": "user", "content": user_prompt}],
        "max_tokens": 4000,
        "temperature": 0.7,
        "stream": True,
    }
    response = requests.post(
            f"{API_URL}/chat/completions",
            stream=True,
            headers=headers,
            data=json.dumps(data)
        )

    # Check if the response is valid before proceeding
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return

    client = sseclient.SSEClient(response)
    for event in client.events():
        if event.data != '[DONE]':
            print(json.loads(event.data)['choices'][0]['text'], end="", flush=True)

if __name__ == '__main__':
    request_with_stream(prompt)