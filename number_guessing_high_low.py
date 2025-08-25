import random

high = 100
low = 1
guesses = 0

number = random.randint(low, high)
running = True
print(f"Welcome! Please guess the number between {low} - {high}. Good luck!")
while running:
    guess = input("Please guess the number: ")
    guesses += 1
    if guess.isdigit():
        guess = int(guess)
        if guess < low or guess > high:
            print(
                f"The number is out of range! Please only guess number between {low} & {high}#: ")
        elif guess < number:
            print("Higher...")
        elif guess > number:
            print("Lower...")
        else:
            print(
                f"After {guesses} guesses, you got it! The number was {number}!")
            running = False
    else:
        print(
            f"Invalid! Please only guess number between {low} & {high}. \nPlease guess the number: ")
