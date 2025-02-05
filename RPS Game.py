""" WORKFLOW OF PROJECT:
1-Input from user (rock,pepar,scissor )
1-cumputer choice(randomly)
3-result print

CASES:
A- ROCK
ROCK - ROCK= tie
ROCK - PAPER= PAPER wil win
ROCK - SCISSOR= ROCK will win 

B - PAPER 
PAPER - ROCK=PAPER wil win
PAPER - PAPER= tie
PAPER - SCISSOR= SCISSOR will win 

C - SCISSOR
SCISSOR - ROCK= ROCK wil win
SCISSOR - PAPER= SCISSOR will win
SCISSOR - SCISSOR= tie

"""
import random
item_list =["Rock","Paper","Scissor"]
     
user_choice = input("Enter your move= Rock/Paper/Scissor :")
comp_choice =random.choice(item_list)
print("user choice=", user_choice)
print("computer choice=", comp_choice)
if user_choice ==comp_choice:
     print("both chooses same: match is TIE")
elif user_choice=="Rock":

    if comp_choice == "Paper":
        print("computer Won")
    else:
        print("YOU Won")
elif user_choice=="Paper":
    if comp_choice == "Rock":
        print("YOU Won")
    else:
        print("computer Won")
elif user_choice=="Scissor":
    if comp_choice == "Rock":
        print("computer Won")
    else:
        print("computer Won")







