#  File: EasterSunday.py

#  Description: This program tells computes the date of Easter Sunday given a certain year.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 1/29/16

#  Date Last Modified: 1/31/16


def main():
    #Prompt user to enter a year
    year = eval ( input ("Enter year: ") )
    
    #Compute date of Easter Sunday
    y = year
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    
    if (n == 3):
        n = "March."
    elif (n == 4):
        n = "April."
    
    #Show output of Easter Sunday's date
    print (" ")
    print ("In" , y , "Easter Sunday is on" , p, n)
    
main() 