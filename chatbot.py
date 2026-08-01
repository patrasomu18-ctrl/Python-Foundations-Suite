# Basic Chatbot

def chatbot():
    print("=================================")
    print("      Welcome to Basic Chatbot")
    print("Type 'bye' to exit the chat.")
    print("=================================")

    while True:
        user = input("\nYou: ").lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: My name is Python Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
