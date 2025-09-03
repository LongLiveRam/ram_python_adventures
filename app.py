import random


def get_random_word():
    """
    Returns a random word from a predefined list.
    """
    words = ["python", "hangman", "challenge",
             "programming", "developer", "computer", "algorithm"]
    return random.choice(words)


def display_game_state(word, guessed_letters):
    """
    Displays the current state of the game, including the word with blanks
    and the letters that have already been guessed.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display)


def display_hangman(incorrect_guesses):
    """
    Displays the hangman figure based on the number of incorrect guesses.
    """
    stages = [
        # Stage 0: empty
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        # Stage 1: head
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        # Stage 2: body
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        # Stage 3: one arm
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        # Stage 4: two arms
        """
           -----
           |   |
           |   O
           |  /|\\
           |
           -
        """,
        # Stage 5: one leg
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        # Stage 6: two legs (final stage)
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """
    ]
    if incorrect_guesses < len(stages):
        print(stages[incorrect_guesses])


def play_hangman():
    """
    The main function to run the hangman game.
    """
    word_to_guess = get_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        print("\nWord:", end=" ")
        display_game_state(word_to_guess, guessed_letters)
        print(
            f"\nIncorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {sorted(guessed_letters)}")

        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid guess. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct!")
            # Check if the player has won
            if all(letter in guessed_letters for letter in word_to_guess):
                print(
                    f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

    # Game over logic
    if incorrect_guesses == max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        print("\nGame Over!")
        print(f"The word was: {word_to_guess}")


# Start the game
if __name__ == "__main__":
    play_hangman()
