from prompt_templates import text_analysis
from tools import llm

selected_model = "gpt-4-1106-preview"

# The input of the sentence 
sentence = "I had a very good day yesterday!"

def analyze_sentiment(sentence):
    prompt = text_analysis.sentiment_analysis_numbers.format(sentence = sentence )
    response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)
    return response 

result = analyze_sentiment(sentence)

print("Joe's Slave 💩: \n", result)
