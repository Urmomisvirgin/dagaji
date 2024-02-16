from functions import llm, helpers
from prompt_templates import productivity

selected_model = "gpt-3.5-turbo"

input_prompt = "generate catchy youtube titles for a video about [topic]"

prompt = productivity.prompt_generator.format(basic_prompt = input_prompt)

response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)

# counting the number of tokens for INPUT and store it in the variable token_count 
token_count = helpers.count_tokens(prompt,selected_model)

# estimating the cost of INPUTs based on token_count, taking into account the model and service
cost = helpers.estimate_input_cost(selected_model,token_count)

# showing the cost of this operation
print(f" \n 💸 Cost: {cost} Dollars \n")
print("--------------------------------------------")

print("Joe's Slave 💩: \n", response)