from functions import helpers, llm, serp 
from prompt_templates import blogging

selected_model = "gpt-3.5-turbo"

query = "chatgpt tricks"

search_result = serp.search_google(query, 3)


for result in search_result:
    print(f"📖️ Summary For: {result}")
    print("--------------------------------")
    transcript = helpers.get_article_from_url(
        result
    ) # change the prompt to whatever you want 

    prompt = blogging.blog_bullet_summary_prompt.format(MaxPoints = "10" , MinPoints = "5", InputText = transcript)

    response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)

    print("Joe's Slave 💩: \n", response)
    print("----------------------------------")









