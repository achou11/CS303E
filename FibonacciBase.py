# FibonacciBase.py

# Description: Program converts computes Fibonacci base representation of a decimal number.

# Student Name: Andrew Chou

# Student UT EID: aoc349

# Course Name: CS 303E

# Unique Number: Morning (50860)

# Date Created: 4/29/16

# Date Last Modified: 4/29/16

# Create list of Fibonacci sequence based on input decimal number
def create_FibSeq(num):
    fib_list = []
    if num == 0:
        fib_list.append(0)
    
    f0 = 0
    f1 = 1
    f = f0 + f1

    while f <= num:
        
        fib_list.append(f)
        f0 = f1
        f1 = f
        f = f0 + f1
        
        if f > num:
            break

    return fib_list
    
    
#Function to convert number into Fibonacci base
def convert_fib_base(num, fib_list):
    # Create dictionary of fib list
    fib_dict = {}
    
    # Create variable to represent remainder of input number
    remainder = num
    
    # Create string variable for fib base representation
    binary = ''
    
    # Go through each element in Fibonacci Sequence to check if value is within the input number
    fib_list.reverse()
    
    for i in range(len(fib_list)):
        if remainder >= fib_list[i]:
            remainder -= fib_list[i]
            fib_dict[fib_list[i]] = 1
        else:
            fib_dict[fib_list[i]] = 0
    
    # Fill representation string with binary
    for ele in fib_list:
        binary += str(fib_dict[ele])

    
    return binary
    
    
def main():
    
    # Ask user for decimal number input
    print()
    dec_num = eval(input("Enter a number: "))
    
    # Create Fibonacci sequence
    fib_seq = create_FibSeq(dec_num)
    
    # Compute fib base binary representation of input number
    bin_rep = convert_fib_base(dec_num, fib_seq)

    # Print statement
    print(str(dec_num) + " = " + bin_rep + " (fib)")
    print()
    
main()  
    