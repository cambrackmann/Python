#!/usr/local/bin/python3

import random

computer = random.randint(0,2)

if computer == 0:
    computer = "Rock"
elif computer == 1:
    computer = "Paper"
elif computer == 2:
    computer = "Scissors"

user = input("Rock, Paper, Scissors?  ")

if user == "Rock" or "rock":
    if computer == "Rock":
        print("It's a draw! Rock v Rock")
    elif computer == "Paper":
        print ("You lose! Paper beats Rock")
    elif computer == "Scissors":
        print ("You win, you amazing bastard! Rock beats Scissors")

elif user == "Paper" or "paper":
    if computer == "Rock":
        print("You win, you amazing bastard! Paper beats Rock")
    elif computer == "Paper":
        print ("It's a draw! Paper v Paper")
    elif computer == "Scissors":
        print ("You lose! Scissors beats Paper")

elif user == "Scissors" or "scissors":
    if computer == "Rock":
        print("You lose! Rocks beats Scissors")
    elif computer == "Paper":
        print ("You win, you amazing bastard! Scissors beats Paper")
    elif computer == "Scissors":
        print ("It's a draw! Scissors v Scissors")
