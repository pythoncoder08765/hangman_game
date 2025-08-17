import random

def hangman():
    # List of predefined words
    words = ["python", "program", "hangman", "random", "string"]

    # Choose a random word
    word = random.choice(words)
    guessed = ["_"] * len(word)   # Hide letters with underscores
    attempts = 6                  # Maximum wrong guesses
    guessed_letters = []          # Keep track of letters already guessed

    print("🎯 Welcome to Hangman Game!")
    print("You have 6 incorrect guesses allowed.")
    print("Word to guess:", " ".join(guessed))

    # Main game loop
    while attempts > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()

        # Check valid input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print("Word:", " ".join(guessed))
        print("Guessed letters:", ", ".join(guessed_letters))

    # Game result
    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game Over! The word was:", word)


# Run the game
if __name__ == "__main__":
    hangman()
