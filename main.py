from tools import helpers, llm
from prompt_templates import blogging, productivity, twitter,text_analysis, ideas

selected_model = "gpt-3.5-turbo"
# user_message = input ("😎 Joe Xu: ")
input_text = """give me some ideas about the """

# Calling the prompts and inputting the parameters accordingly to use as the prompts that I input for LLMs
prompt = input_text

# counting the number of tokens for INPUT and store it in the variable token_count 
token_count = helpers.count_tokens(prompt,selected_model)

# estimating the cost of INPUTs based on token_count, taking into account the model and service
cost = helpers.estimate_input_cost(selected_model,token_count)

# call llm generate function to get response from LLMs
response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)

print(f" \n 💸 Cost: {cost} Dollars \n")

print("🐶💩 Joe's Slave: \n \n" + response)







