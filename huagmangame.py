import random

def play_hangman():
    # 1. Small list of 5 predefined words
    word_list = ["python", "vscode", "coding", "streamlit", "laptop"]
    
    # Randomly select a secret word
    secret_word = random.choice(word_list)
    
    # Game setup tracking variables
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("====================================")
    print("      WELCOME TO HANGMAN GAME!      ")
    print("====================================")
    print(f"Guess the word letter by letter. You have {max_incorrect_guesses} wrong attempts.\n")
    
    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Build display string with guessed letters or underscores
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"Word: {display_word.strip()}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Incorrect attempts remaining: {max_incorrect_guesses - incorrect_guesses}\n")
        
        # Check for victory condition (no underscores left)
        if "_" not in display_word:
            print("🎉 CONGRATULATIONS! You guessed the word correctly!")
            print(f"The secret word was: {secret_word.upper()}\n")
            break
            
        # Get user input
        guess = input("Enter a letter: ").lower().strip()
        
        # Input validation logic
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.\n")
            continue
        elif guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try another one.\n")
            continue
            
        # Record guess
        guessed_letters.append(guess)
        
        # Check if guess is correct or incorrect using if-else
        if guess in secret_word:
            print(f"✅ Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"❌ Wrong guess! '{guess}' is not in the word.\n")
            
    # Check for loss condition
    if incorrect_guesses == max_incorrect_guesses:
        print("====================================")
        print("💥 GAME OVER! You ran out of attempts.")
        print(f"The secret word was: {secret_word.upper()}")
        print("====================================\n")

# Run the game
if __name__ == "__main__":
    play_hangman()