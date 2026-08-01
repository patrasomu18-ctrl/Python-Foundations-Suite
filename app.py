import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Python Foundations Suite", page_icon="⚡", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
choice = st.sidebar.radio("Select an Application:", ["Home / Dashboard", "🤖 Rule-Based Chatbot", "🎮 Terminal Hangman"])

# ---------------------------------------------------------
# 🏠 HOME / DASHBOARD PAGE
# ---------------------------------------------------------
if choice == "Home / Dashboard":
    st.title("⚡ Python Foundations Suite")
    st.subheader("Welcome to the Interactive App Hub")
    st.write(
        "Choose an application from the sidebar on the left to get started!"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("### 🤖 Rule-Based Chatbot\nAn interactive web chatbot demonstrating custom rule-based responses and Streamlit state management.")
        
    with col2:
        st.success("### 🎮 Terminal Hangman\nAn interactive, web-adapted classic word-guessing game built using core Python control logic.")

# ---------------------------------------------------------
# 🤖 CHATBOT PAGE
# ---------------------------------------------------------
elif choice == "🤖 Rule-Based Chatbot":
    st.title("🤖 Rule-Based Chatbot")
    st.caption("Ask me anything about Python, projects, or common queries!")

    # Chatbot logic goes here
    # Example state initialization:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("Say something..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Simple Rule-Based Logic
        response = "I'm a rule-based assistant! How can I help you today?"
        if "hello" in user_input.lower():
            response = "Hello! Welcome to the suite."
        elif "python" in user_input.lower():
            response = "Python is a powerful and versatile programming language!"

        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

# ---------------------------------------------------------
# 🎮 HANGMAN GAME PAGE
# ---------------------------------------------------------
elif choice == "🎮 Terminal Hangman":
    st.title("🎮 Hangman Game")
    st.caption("Guess the word letter by letter before running out of attempts!")

    # Words list & Game state
    words = ["PYTHON", "STREAMLIT", "GITHUB", "DEVELOPER", "CHATBOT"]
    
    if "secret_word" not in st.session_state:
        st.session_state.secret_word = random.choice(words)
        st.session_state.guessed_letters = set()
        st.session_state.attempts = 6

    secret_word = st.session_state.secret_word
    guessed_letters = st.session_state.guessed_letters

    # Display Word Mask
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    st.markdown(f"## `{display_word}`")
    st.write(f"❤️ Attempts remaining: **{st.session_state.attempts}**")

    # Game Controls
    if st.session_state.attempts > 0 and "_" in display_word:
        guess = st.text_input("Enter a letter:", max_chars=1).upper()
        
        if st.button("Submit Guess") and guess:
            if guess in guessed_letters:
                st.warning("You already guessed that letter!")
            elif guess in secret_word:
                guessed_letters.add(guess)
                st.success(f"Good job! '{guess}' is in the word.")
                st.rerun()
            else:
                guessed_letters.add(guess)
                st.session_state.attempts -= 1
                st.error(f"Wrong guess! '{guess}' is not in the word.")
                st.rerun()

    # Win / Lose State
    if "_" not in display_word:
        st.balloons()
        st.success("🎉 Congratulations! You guessed the word!")
        if st.button("Play Again"):
            del st.session_state.secret_word
            st.rerun()
    elif st.session_state.attempts <= 0:
        st.error(f"💀 Game Over! The word was: **{secret_word}**")
        if st.button("Try Again"):
            del st.session_state.secret_word
            st.rerun()