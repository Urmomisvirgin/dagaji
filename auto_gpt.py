from functions import llm, helpers 
from prompt_templates import productivity

selected_model = "gpt-3.5-turbo"

#input_text = "get me the latest price of bitcoin"
input_text = "extract the main points of the following text: [text...]"
#input_text = "translate the following text into english: [text...]"


prompt = productivity.auto_gpt_prototype.format(user_input = input_text)

response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)

if response =="1":
    # simulate web search 
    print("searching the web ...")
if response == "2":
    #simulate summarizing
    print("summarizing ...")
if response == "3":
    #simulate translation
    print("translating ...")



