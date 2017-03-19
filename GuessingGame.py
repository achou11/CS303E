#  File: GuessingGame.py

#  Description: This program guesses a user's input number between 1 and 100.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS 303E

#  Unique Number: Morning (50860)

#  Date Created: 4/10/16

#  Date Last Modified: 4/12/16

def main():

#Initial print statements
    print ("Guessing Game \n")

    print("Think of a number between 1 and 100 inclusive. \nAnd I will guess what it is in 7 tries or less. \n")

#Check if user is ready to play  
    askPlay = input ("Are you ready? (y/n): ")
    
    while (askPlay != "y" and askPlay != "n"):
        askPlay = input ("Are you ready? (y/n): ")
        
    if askPlay == "n":
        print("Bye")
        return
    
    else:
        
        #Initialize hi, lo, and count variables
        hi = 100
        lo = 0
        count = 1
        
        #Loop for computing guesses to user responses
        while count < 8:
            guess = (hi + lo) // 2
            print("\nGuess  " + str(count) + " : The number you thought of was " + str(guess))
            response = int (input ("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
            
            #Check if response is within range
            while (response != -1 and response != 0 and response != 1):
                response = int (input ("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
            
            #Answer for when the guess is low
            if (response == -1):
                lo = guess + 1
                guess = (hi + lo) // 2
                count += 1
            #Answer for when the guess is high
            elif (response == 1):
                hi = guess - 1
                guess = (hi + lo) // 2
                count += 1
            #Answer for when the guess is correct
            elif (response == 0):
                print ("\nThank you for playing the Guessing Game.")
                break
            
            #Output for when number of guesses exceeds 7
            if (count == 8):
                print ("Either you guessed a number out of range or you had an incorrect entry.")
                break


#Call main
main()