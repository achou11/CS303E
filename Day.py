#  File: Day.py

#  Description: This program prints the day of the week when given the year, month, and day of the month.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 1/31/16

#  Date Last Modified: 2/4/16

def main():
    #Prompt user to enter year
    year = eval ( input ("Enter year: "))
    while (year < 1900 or year > 2100):
        year = eval ( input ("Enter year: "))
        
    #Prompt user to enter month
    month = eval ( input ("Enter month: "))
    while (month < 1 or month > 12):
        month = eval ( input ("Enter month: "))
    if (month == 1 or month == 2):
        year = year - 1
        
    #Prompt user to enter day of month
    day = eval ( input ("Enter day: "))
    
    #Determine if year is leap year or not
    is_leap = (year % 400 == 0) and ( (year % 4 == 0) or (year % 100 != 0) )
    
    #Compute number of days in a month
    num_days = 0
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 11):
        num_days = 31
    elif (month == 4 or month == 6 or month == 9 or month == 11):
       num_days = 30
    elif (month == 2):
        num_days = 28
        if (is_leap):
            num_days = 29
      
    while (day < 1 or day > num_days):
        day = eval( input ("Enter day: "))
        
    
    #Compute day of week
    a = 0
    if (month == 1):
        a = 11
    elif (month == 2):
        a = 12
    elif (month == 3):
        a = 1
    elif (month == 4):
        a = 2
    elif (month == 5):
        a = 3
    elif (month == 6):
        a = 4
    elif (month == 7):
        a = 5
    elif (month == 8):
        a = 6
    elif (month == 9):
        a = 7
    elif (month == 10):
        a = 8
    elif (month == 11):
        a = 9
    elif (month == 12):
        a = 10
    
    b = day
    
    c = year % 100
    
    d = year // 100
    
    w = (13 * a - 1 ) // 5 

    x = c // 4 

    y = d // 4 

    z = w + x + y + b + c - 2 * d 

    r = z % 7 

    r = (r + 7) % 7
    
    if (r == 0):
        day_of_week = "Sunday."
    elif (r == 1):
        day_of_week = "Monday."
    elif (r == 2):
        day_of_week = "Tuesday."
    elif (r == 3):
        day_of_week = "Wednesday."
    elif (r == 4):
        day_of_week = "Thursday."
    elif (r == 5):
        day_of_week = "Friday."
    elif (r == 6):
        day_of_week = "Saturday."
        
    #Show output of day of week
    print ()
    print ("The day is", day_of_week)

main()