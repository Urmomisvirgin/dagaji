# Content classification 
simple_classification_prompt = """Your task as a text analyzer is to classify a given sentence into one of the specific categories: 'food', 'sports', or 'business'. In doing so, you must carefully consider the main theme and context of the sentence. Your response should clearly communicate your classification choice for the sentence and provide a brief explanation that highlights key elements, such as words or phrases, that support your decision.

Please note that your analysis should be adaptable, flexible, and capable of addressing a wide range of sentence types and structures. Your objective is to deliver a precise, accurate, and insightful categorization that demonstrates an in-depth understanding of the main theme and context of the sentence while focusing on the designated categories.

Input Sentence: [{sentence}]"""




# Information extraction 
information_extraction = """As a text analyzer, your objective is to examine a given text and extract essential information in response to a specific query. Your task involves accurately identifying key data related to the query, demonstrating an in-depth understanding of the source material, and presenting your findings in a concise and coherent manner, preserving the context of the information.

Please note that your response should be versatile enough to handle a wide variety of texts and queries. You are expected to effectively adapt your analysis strategy to locate relevant details across diverse scenarios. Ensure that your focus remains on accuracy, clarity, and relevance while addressing the specific query provided.

here is the query: [{query}]"""


# sentiment analysis
sentiment_analysis = """I will provide you with a sentence, and I want you to analyze the sentiment, and return back Positive, Negative, Neutral. reply with just one word. 
sentence: [{sentence}]"""

sentiment_analysis_numbers = """I will provide you with a sentence, and I want you to analyze the sentiment, and return back 1 is positive, -1 is negative, 0 if neutral. reply with just one number. 
sentence: [{sentence}]"""



