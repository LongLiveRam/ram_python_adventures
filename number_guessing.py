import random

# number guessing game
running = True
while running:
    random_number = random.randint(1, 6)
    player_guess = input("Please guess a number between 1 - 6 (q to quit): ")
    if player_guess.lower() == "q":
        print("Thanks for playing!!!")
        running = False
    elif random_number == int(player_guess):
        print(f"You got it right! The number was {random_number}.")
    else:
        print(f"You guessed wrong! The number was {random_number}.")
