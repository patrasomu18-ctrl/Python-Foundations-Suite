import streamlit as st

# Function to get predefined responses based on user input
def chatbot_reply(user_input):
    user_input = user_input.lower().strip()
    
    # if-elif conditional statements
    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that yet. Try typing 'hello', 'how are you', or 'bye'."

# Title
st.title("TASK 4: Basic Chatbot")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Loop through history and display past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input field
if user_prompt := st.chat_input("Type 'hello', 'how are you', or 'bye'..."):
    # Display user message
    with st.chat_message("user"):
        st.write(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Get reply from function
    reply = chatbot_reply(user_prompt)

    # Display bot message
    with st.chat_message("assistant"):
        st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})