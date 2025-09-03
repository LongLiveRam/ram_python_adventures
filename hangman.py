# The program must have a pre-defined list of words to choose from. ✅
# It should randomly select one word from this list for the user to guess. ✅
# The game should have a set number of allowed incorrect guesses (e.g., 6).
# The program must track the letters the user has already guessed. ✅
# After each guess, the game must display the state of the word, showing correctly guessed letters and blanks for the unguessed ones. ✅
# The user should be prompted to enter a single letter. ✅
# The program must handle cases where the user enters a non-letter, a letter they've already guessed, or more than one letter. ✅
# The game should continue in a loop until the user either guesses the full word or runs out of guesses. ✅
# At the end, the program should announce whether the user won or lost. ✅

import random

words = ["jazz", "mystery", "zombie",      "phoenix", "gymnast", "oxygen", "wizard", "flamingo", "rythm", "hyphen",
         "quintuple", "vampire", "puzzle", "luck", "keyboard", "whistle", "uniform", "gazelle", "equation", "luxury"]


def pick_word():
    return random.choice(words)


def display_status(word_to_guess, guessed_letters):
    display = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display)


def welcome(max_guesses):
    print(
        f"Welcome to Hangman! You have a total of {max_guesses} to save this man! Good luck!\n(\"qq\" to quit or \"rs\" to restart)")


def quit():
    print("Thanks for playing...")
    return False


def play_hangman():
    running = True
    incorrect_guesses = 0
    max_guesses = 6
    guessed_letters = []
    word_to_guess = pick_word()

    welcome(max_guesses)
    while running:

        if incorrect_guesses == max_guesses:
            print("You lost!")
            break

        print("\nWord:", end=" ")
        display_status(word_to_guess, guessed_letters)
        print(f"You have {max_guesses - incorrect_guesses} left!")
        print(sorted(guessed_letters))

        guess = input("Please enter a letter:").lower().strip()
        # Quit and restart option for user
        if guess == "qq":
            running = quit()
        elif guess == "rs":
            incorrect_guesses = 100
        elif not guess.isalpha() or len(guess) != 1:
            print("Invalid! Please enter a single letter!")
            continue
        elif guess in guessed_letters:
            print("You've already guessed this letter!")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("You guessed a letter correctly!")
            if all(letter in guessed_letters for letter in word_to_guess):
                print("Noice! You won!")
                break
        else:
            print("That was the wrong letter!")
            incorrect_guesses += 1


if __name__ == "__main__":
    while True:
        play_hangman()

        play_again = input(
            "\nDo you want to play again? (y/n): ").lower().strip()
        if play_again != 'y':
            break
        else:
            print("Restarting... Randomly picking a word...")
