import streamlit as st
from google import genai

# 1. Setup API Key input in the sidebar
st.sidebar.title("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

st.title("🤖 Real-Time AI Chatbot")
st.write("Ask me anything!")

# 2. Initialize chat session and history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages on screen
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 3. User input handling
if user_prompt := st.chat_input("Ask me any question..."):
    if not api_key:
        st.error("Please enter your Gemini API Key in the left sidebar first!")
    else:
        # Show user message
        with st.chat_message("user"):
            st.write(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})

        try:
            # Connect to Gemini API
            client = genai.Client(api_key=api_key)
            
            # Generate AI response
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_prompt,
            )
            bot_reply = response.text

            # Show bot reply
            with st.chat_message("assistant"):
                st.write(bot_reply)
            st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

        except Exception as e:
            st.error(f"Error connecting to AI: {e}")