# File: Deal.py

# Description: This program simulates the game show, Let's Make a Deal.

# Student Name: Andrew Chou

# Student UT EID: aoc349

# Course Name: CS 303E

# Unique Number: Morning (50860)

# Date Created: 3/2/16

# Date Last Modified: 3/4/16

# Import necessary modules
import random

# Create a function that simulates game
def main():
    
    print()
    
    ask = eval ( input ("Enter number of times you want to play: ") )
    
    print()
    
    print ( "{:^9}".format("Prize") + "{:^13}".format("Guess") + "{:^10}".format("View") + "{:^11}".format("New Guess") )  
    
    switch_wins = 0
    
    for rounds in range(1, ask + 1):
        
        prize = random.randint(1, 3)
        
        guess = random.randint(1, 3)
        
        view = 0
        
        if (prize != guess):
            view = 6 - (prize + guess)
        else: 
            view = random.randint(1, 3)
            while (view == prize):
                view = random.randint(1, 3)
        
        newGuess = 6 - (guess + view)
        
        if (newGuess == prize):
            switch_wins += 1
        
        # Print correctly formatted result 
        print ( "{:^9}".format(prize) + "{:^13}".format(guess) + "{:^9}".format(view) +"{:^13}".format(newGuess) )
    
    # Calculate probability of winning if person does or doesn't switch   
    prob_win_switch = switch_wins / ask
    prob_win_stay = 1 - prob_win_switch
    
    print()
    print ( "Probability of winning if you switch =", "{:04.2f}".format(prob_win_switch) )
    print ( "Probability of winning if you do not switch =", "{:04.2f}".format(prob_win_stay) )
    print()


main()

