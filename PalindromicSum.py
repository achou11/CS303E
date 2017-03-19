#  File: PalindromicSum.py

#  Description: This program repeatedly reverses the digits of a number and adds it to itself until it is palindromic. It then prints out the number with the largest cycle length and its respective length.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS 303E

#  Unique Number: Morning (50860)

#  Date Created: 2/18/16

#  Date Last Modified: 2/19/16


# reverse the digits of a number
def rev_num(n):
  rev_n = 0
  while (n > 0):
    rev_n = rev_n * 10 + (n % 10)
    n = n // 10
  return rev_n


# determines if a number is palindromic
def is_palindromic(n):
  return (n == rev_num(n))


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
    while (not is_palindromic(num)):
      num += rev_num(num)
        
      # increment cycle_length
      cycle_length += 1
      
    # compare the cycle length of a number with the max cyclelength and
    # replace max cycle length if cycle length of number is greater or equal

    if (cycle_length >= max_cycle_length):
      max_cycle_length = cycle_length
      max_num = counter
      
    counter += 1

  # print the result
  print ("The number " + str(max_num) + " has the longest cycle length of " + \
  str(max_cycle_length) + ".")
  print()


main()