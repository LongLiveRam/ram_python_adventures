# Make a rock, paper, scissor game using the random class

import random

options = ("rock", "paper", "scissor")
computer_score = player_score = tie = 0
running = True
# more improved version of the logic for detecting player wins. (asked from Gemini)
winning_combinations = [
    ("paper", "rock"), ("scissor", "paper"), ("rock", "scissor")]
while running:
    print(
        f"Score: Player = {player_score} | Computer = {computer_score} | Tie = {tie}")
    computer_guess = random.choice(options)
    player_guess = input(
        "Please enter your guess (rock, paper, scissor) (q to quit): ").lower()
    if player_guess.lower() == "q":
        print("Thanks for playing!!")
        running = False
    elif player_guess == computer_guess:
        print("Tie!")
        tie += 1
    elif (player_guess, computer_guess) in winning_combinations:
        print(
            f"Computer picked {computer_guess} and player picked {player_guess}\nPlayer wins!")
        player_score += 1
    else:
        print(
            f"Computer picked {computer_guess} and player picked {player_guess}\nComputer wins!")
        computer_score += 1
