#  File: ISBN.py

#  Description: This program reads if a given string of characters is a valid ISBN.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS 303E

#  Unique Number: Morning (50860)

#  Date Created: 3/31/16

#  Date Last Modified: 4/1/16

#Function to check ISBN length
def isbn_len(x):
    if len(x) != 10:
        return False

#Function to if ISBN is has appropriate types of characters
def isbn_dig(x):
    isbn_sub = x[0:9]
    for i in isbn_sub:
        if (i.isdigit() == False):
            return False

#Function to calculate first partial sum
def partial1(sum_1):
    list1 = []
    sum = 0
    for i in sum_1:
        if sum_1[-1] == "X" or sum_1[-1] == "x":
            sum_1[-1] = 10
            sum += int(i)
        else:
            sum += int(i)
        list1.append(sum)
        
    return list1

#Function to calculate second partial sum
def partial2(sum_2):
    list2 = []
    sum = 0
    for i in sum_2:
        sum += int(i)
        list2.append(sum)
        
    return list2

#Function to check if second partial sum is divisible by 11
def is_mod11(value):
    if value % 11 != 0:
        return False

def main():

    #Open 'isbn.txt' for reading and create another file for writing
    
    in_file = open("isbn.txt", "r")
    outfile = open("isbnOut.txt", "w")
    
    #Loop through each line in the in_file

    for line in in_file:
        isbn_print = line.strip()
        isbn = isbn_print.replace("-","")
        isbn = list(isbn)
    
        #ISBN validity checks

        if isbn_len(isbn) == False:
            outfile.write(str.ljust(isbn_print, 15) + "invalid\n")
          
        elif isbn_len(isbn) != False:
        
            if isbn_dig(isbn) == False:
                outfile.write(str.ljust(isbn_print, 15) + "invalid\n")
            
            elif isbn_dig(isbn) != False:
                list1 = partial1(isbn)
                list2 = partial2(list1)
                
                if is_mod11(list2[-1]) == False:
                    outfile.write(str.ljust(isbn_print, 15) + "invalid\n")
                
                elif is_mod11(list2[-1]) != False:
                    outfile.write(str.ljust(isbn_print, 15) + "valid\n")
                    
    #Close files
    
    in_file.close()
    outfile.close()
    
main()


















