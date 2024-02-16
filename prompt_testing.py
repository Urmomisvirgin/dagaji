from functions import helpers, llm

selected_model = "gpt-3.5-turbo"

test_prompt = """As a YouTube content creator, your goal is to come up with attention-grabbing and compelling titles for videos related to [topic]. Keep in mind the target audience and try to invoke curiosity, appeal to emotions, and provide a clear benefit or value proposition in the titles. The title should be concise but descriptive. Aim to generate at least three catchy YouTube titles that will entice viewers to click and watch the video.

Please generate 5 catchy YouTube titles for a video about [topic]. Make sure the titles are optimized for maximum click-through rates and reflect a good balance of being engaging and informative.
"""

input_list = [
    "email marketing", # easy 
    "bitcoin trading", # medium 
    "advanced prompt engineering techniques", # hard
]

for input in input_list:
    prompt = test_prompt.replace("topic", input)
    response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)
    print(f"Result for [{input}]")
    print("Joe's Slave 💩: \n", response)
    print("----------------------------------")

