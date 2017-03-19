#  File: Goldbach.py

#  Description: This program verifies Goldbach's Conjecture for a given range of values.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS 303E

#  Unique Number: Morning (50860)

#  Date Created: 2/24/16

#  Date Last Modified: 2/26/16

#Make a function that checks if a number is prime
def is_prime (n):

  if (n == 1):
    return False

  limit = int(n ** 0.5) + 1
  divisor = 2
  while (divisor < limit):
    if (n % divisor == 0):
      return False
    divisor += 1
  return True


#Go through all numbers in range and print output
def main():
  
  print()  
  lower = eval ( input ("Enter lower limit: ") )
  upper = eval ( input ("Enter upper limit: ") )
  
  while (lower >= upper) or (lower % 2 != 0 or lower < 4) or (upper % 2 != 0 or upper < 4):
    lower = eval ( input ("Enter lower limit: ") )
    upper = eval ( input ("Enter upper limit: ") )    
    
  for num in range ( lower, upper+1, 2 ):
    print (num, end = '')
    for a in range ( 2, ((num // 2) + 1) ):
      b = num - a
      if (is_prime(a) and is_prime(b)):
        print ( " =" , a, "+" , b , end = '' )
    print()


main()