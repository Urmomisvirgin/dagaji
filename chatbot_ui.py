import streamlit as st
import openai

# Streamlit page configuration
st.set_page_config(page_title="Chatbot with GPT-3.5", layout="wide")

# Set OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

# Streamlit cache to store chat history
@st.cache(allow_output_mutation=True)
def get_history():
    return [{"role": "system", "content": "You are a helpful assistant."}]

# Function to continue the chat
def continue_chat(user_message, messages):
    # Add the user's message to the chat history
    messages.append({"role": "user", "content": user_message})

    # Get the chat response from OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the selected model
        messages=messages
    )

    # Add the AI's response to the chat history
    ai_content = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": ai_content})
    return ai_content

# Streamlit UI components
def main():
    # Title of the web app
    st.title("Chat with GPT-3.5")

    # Sidebar for instructions or information
    st.sidebar.title("Instructions")
    st.sidebar.info("Type your message and press enter to chat with the AI. Type 'quit' to end the conversation.")

    # Chat history is stored here
    messages = get_history()

    # Text input for user message
    user_message = st.text_input("Your Message", key="user_input")

    # Display the chat history
    for message in messages:
        if message["role"] == "user":
            st.text_area("", value=message["content"], key=message["content"] + "_user", height=50)
        else:
            st.text_area("", value=message["content"], key=message["content"] + "_assistant", height=50)

    # When the user sends a message
    if st.session_state.user_input:
        if user_message.lower() == "quit":
            st.success("Chat ended. Refresh the page to start over.")
        else:
            # Get the AI's response
            ai_response = continue_chat(user_message, messages)
            # Clear the input box for new message
            st.session_state.user_input = ""

# Run the main function
if __name__ == "__main__":
    main()
