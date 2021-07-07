# Rock, Paper, Scissors game

# we import random as we want python to generate a random output
from random import randint

# moves for the player
moves = ["rock", "paper", "scissors"]

# loop to play the game repeatedly
# .lower() = lowercase any input you give e.g. capital r or all capitals
# == means exactly equals
# elif means if else, then ...
while True:         # loop requires a colon
    computer = moves[randint(0, 2)]     # computer returns a random element from 0 to 2 , non-biased
    player = input("rock, paper or scissors? (or end the game) ").lower()    # what we'll see on the terminal
    if player == "end the game":
        print("The game has ended.")
        break                           # breaks the while True
    elif player == computer:        # tie
        print("Tie!")
    elif player == "rock":          # outcomes for rock
        if computer == "paper":     # use paper, as paper beats rock
            print("You lose!", computer, "beats", "player")     # i.e. paper beats player, who played rock
        else:
            print("You win!", player, "beats", computer)       # i.e. player played scissors
    elif player == "paper":             # outcomes for paper
        if computer == "scissors":      # use scissors, as scissors beats paper
            print("You lose!", computer, "beats", "player")  # i.e. scissors beats player, who played paper
        else:
            print("You win!", player, "beats", computer)    # i.e. player played rock
    elif player == "scissors":             # outcomes for scissors
        if computer == "rock":      # use rock, as rock beats scissors
            print("You lose!", computer, "beats", "player")     # i.e. rock beats player, who played scissors
        else:
            print("You win!", player, "beats", computer)    # i.e. player played paper
    else:
         print("Check your spelling ...")   # in case there are typos