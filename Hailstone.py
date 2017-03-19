#  File: Hailstone.py

#  Description: Given a range of numbers, this program prints out the number with the largest cycle length and its respective length.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS303E

#  Unique Number: 50860

#  Date Created: 2/6/16

#  Date Last Modified: 2/9/16


def main():
  
  # prompt the user to enter the starting number
  print()
  start = eval ( input ("Enter starting number of the range: ") )
  print()

  # prompt the user to enter the ending number
  finish = eval ( input ("Enter ending number of the range: ") )
  print()
  
  # initialize the variables to hold number and max cycle length
  max_num = 0
  max_cycle_length = 0

  # check to see if range values are valid
  while ( start <= 0 or finish <= 0 or finish < start ):
    start = eval ( input ("Enter starting number of the range: ") )
    print()
    finish = eval ( input ("Enter ending number of the range: ") )
    print()
  
  # determine the number having the largest cycle length in this range
  # write a loop that goes through all the numbers in that range
  counter = start
  while (counter <= finish):
   
    # determine the cycle length of each number
    cycle_length = 0
    num = counter
    while (num > 1):
      if (num % 2 == 0):
        num = num // 2 
      else:
        num = 3 * num + 1
        
      # increment cycle_length
      cycle_length = cycle_length + 1
      
    # compare the cycle length of a number with the max cyclelength and
    # replace max cyclelength if cycle length of number is greater or equal

    if (cycle_length >= max_cycle_length):
      max_cycle_length = cycle_length
      max_num = counter
      
    counter = counter + 1

  # print the result
  print ("The number " + str(max_num) + " has the longest cycle length of " + \
  str(max_cycle_length) + ".")
  print()


main()