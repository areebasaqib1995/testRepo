# Acknowledgement:
# I co-created this code with the help of ChatGPT (OpenAI GPT-5).
# Numly - 3-Digit Number Guessing Game
# feature 1: 5 attempt allowed only
# Features 2: limited guesses + feedback system (P/M/X)


import random

class NumlyGame:
    """3-digit number guessing game with limited guesses and feedback."""

    def __init__(self):
        # Computer chooses a random 3-digit number
        self.secret_number = random.randint(100, 999)

    def play(self):
        MAX_ATTEMPTS = 5  # maximum guesses per player
        attempts = 0

        print("Welcome to Numly – 3-digit Number Guessing Game!")
        print("Try to guess the number between 100 and 999.")
        print("Type 'exit' anytime to quit the game.\n")
        print("P= perfect in position and number, M= correct number but incorrect position, x= number not present")

        while True:
            # input
            guess = input(f"Enter your guess (Attempt {attempts + 1}/{MAX_ATTEMPTS}): ")

            # Exit option
            if guess.lower() == "exit":
                print("You quit the game. The number was:", self.secret_number)
                break

            # Validate input
            if not guess.isdigit() or len(guess) != 3:
                print("Please enter a valid 3-digit number.\n")
                attempts += 1  # count invalid input as attempt
                if attempts >= MAX_ATTEMPTS:
                    print(f"Maximum attempts reached! The number was: {self.secret_number}")
                    break
                continue

            guess = int(guess)
            attempts += 1

            # Check correct guess
            if guess == self.secret_number:
                print("🎉 You guessed it right! You win!")
                break

            # -------------------------------
            # FEEDBACK SYSTEM (P/M/X)
            # -------------------------------
            guess_str = str(guess)
            secret_str = str(self.secret_number)
            feedback = ""

            for i in range(3):
                if guess_str[i] == secret_str[i]:
                    feedback += "P"  # perfect
                elif guess_str[i] in secret_str:
                    feedback += "M"  # misplaced
                else:
                    feedback += "X"  # not present

            print("Feedback:", feedback)
            print("❌ Wrong guess! Try again.\n")

            # Max attempts reached
            if attempts >= MAX_ATTEMPTS:
                print(f"Maximum attempts reached! The number was: {self.secret_number}")
                break


# Create a game instance and start playing
game = NumlyGame()
game.play()
