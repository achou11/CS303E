#  File: CalculatePI.py

#  Description: This program calculates PI using random numbers and compares it with math.pi value.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS 303E

#  Unique Number: Morning (50860)

#  Date Created: 2/26/16

#  Date Last Modified: 3/2/16

# Import necessary modules
import math
import random

# Create a function that calculates Pi using random numbers
def computePI(numThrows):
    
    sum_darts = 0
    
    for n in range(1, numThrows + 1,):
      
      xPos = random.uniform(-1.0, 1.0)
      yPos = random.uniform(-1.0, 1.0)
      distance = math.hypot (xPos, yPos)
      
      if distance < 1:
        sum_darts += 1
      
      calcPI = 4 * (sum_darts / numThrows)
    
    return calcPI

# Create a function that prints the results for numThrows = 100, 1000, 10000, 100000, 1000000, 10000000
def main():
    
    print()
    
    print ("Computation of PI using Random Numbers")
    
    print()
    
    for n in range(2,8):
        
        num = 10 ** n
        
        calc_PI = computePI(num)
        
        diff = calc_PI - math.pi
         
        # Print correctly formatted result
        print ( str.ljust("num = " + str(num), 17) + \
                str.ljust("Calculated PI = " + str("{:.6f}".format(calc_PI)), 27) + \
                "Difference = " +  str("{:+.6f}".format(diff)) )

    print()
    print ("Difference = Calculated PI - math.pi")
    print()
    
    
main()

