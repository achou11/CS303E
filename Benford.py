#  File: Benford.py

# Description: Program records frequency of the first digit of every line of 2009 Census Data to see if the data adheres to Benford's Law.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS 303E

#  Unique Number: Morning (50860)

#  Date Created: 4/21/16

#  Date Last Modified: 4/21/16

def main():
    # create an empty dictionary
    pop_freq = {}

    # initialize the dictionary
    pop_freq ['1'] = 0
    pop_freq ['2'] = 0
    pop_freq ['3'] = 0
    pop_freq ['4'] = 0
    pop_freq ['5'] = 0
    pop_freq ['6'] = 0
    pop_freq ['7'] = 0
    pop_freq ['8'] = 0
    pop_freq ['9'] = 0

    # open file for reading
    in_file = open ("./Census_2009.txt", "r")
  
    # read the header and ignore
    header = in_file.readline()
  
    # read subsequent lines
    for line in in_file:
        line = line.strip()
        pop_data = line.split()
        # get the last element that is the population number
        pop_num = pop_data[-1]
  
      # make entries in the dictionary
        if (pop_num[0] == '1'):
          pop_freq['1'] += 1
        elif (pop_num[0] == '2'):
          pop_freq['2'] += 1
        elif (pop_num[0] == '3'):
          pop_freq['3'] += 1
        elif (pop_num[0] == '4'):
          pop_freq['4'] += 1
        elif (pop_num[0] == '5'):
          pop_freq['5'] += 1
        elif (pop_num[0] == '6'):
          pop_freq['6'] += 1
        elif (pop_num[0] == '7'):
          pop_freq['7'] += 1
        elif (pop_num[0] == '8'):
          pop_freq['8'] += 1
        elif (pop_num[0] == '9'):
          pop_freq['9'] += 1
    
    # Fill variable 'Total' with the total number of entries so a percentage can be found for each entry  
    total = pop_freq['1'] + pop_freq['2'] + pop_freq['3'] + pop_freq['4'] + pop_freq['5'] + pop_freq['6'] + pop_freq['7'] + pop_freq['8'] + pop_freq['9']
    
    # close the file
    in_file.close()
  
    # Write out the result
    print('Digit'.ljust(9) + 'Count'.ljust(9) + '%')
    
    print('1'.ljust(9) + str(pop_freq['1']).ljust(9) + str(round((pop_freq['1'] / total * 100), 1)))
    print('2'.ljust(9) + str(pop_freq['2']).ljust(9) + str(round((pop_freq['2'] / total * 100), 1)))
    print('3'.ljust(9) + str(pop_freq['3']).ljust(9) + str(round((pop_freq['3'] / total * 100), 1)))
    print('4'.ljust(9) + str(pop_freq['4']).ljust(9) + str(round((pop_freq['4'] / total * 100), 1)))
    print('5'.ljust(9) + str(pop_freq['5']).ljust(9) + str(round((pop_freq['5'] / total * 100), 1)))
    print('6'.ljust(9) + str(pop_freq['6']).ljust(9) + str(round((pop_freq['6'] / total * 100), 1)))
    print('7'.ljust(9) + str(pop_freq['7']).ljust(9) + str(round((pop_freq['7'] / total * 100), 1)))
    print('8'.ljust(9) + str(pop_freq['8']).ljust(9) + str(round((pop_freq['8'] / total * 100), 1)))
    print('9'.ljust(9) + str(pop_freq['9']).ljust(9) + str(round((pop_freq['9'] / total * 100), 1)))
    
main()