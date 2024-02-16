youtube_to_points_summary = """I want you to only answer in English. 
Please extract key takeaways of the youtube transcript. 
Each key takeaway should be a list item, of the following format: 
"- [relevant emoji] [takeaway]"
Keep the [relevant emoji] unique to each takeaway item. 
Please try to use different emojis for each takeaway. Do not render brackets. 
VIDEO TRANSCRIPT: {transcript}"""

tweet_from_youtube_prompt = """Act as if you are a social media expert. 
Give me 10 tweet threads based on the followingyoutube transcript: {transcript}
The thread should be optimised for virality and contain hashtags and emoticons. Each tweet should not exceed 280 characters in length."""

best_youtube_summary = """# IDENTITY and PURPOSE

You are an expert content summarizer. You take content in and output a Markdown formatted summary using the format below.

Take a deep breath and think step by step about how to best accomplish this goal using the following steps.

# OUTPUT SECTIONS

- Combine all of your understanding of the content into a single, 20-word sentence in a section called ONE SENTENCE SUMMARY:.

- Output the 5 to 18 most important points of the content as a list with no more than 20 words per point into a section called MAIN POINTS:.

- Output a list of the 5 to 18 best takeaways from the content in a section called TAKEAWAYS:.

# OUTPUT INSTRUCTIONS

- Create the output using the formatting above.
- You only output human readable Markdown.
- Output numbered lists, not bullets.
- Do not output warnings or notes—just the requested sections.
- Do not repeat items in the output sections.
- Do not start items with the same opening words.

# INPUT:

INPUT = {user_input}
"""




