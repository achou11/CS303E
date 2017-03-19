#  File: Intervals.py

#  Description: This program collapses any overlapping intervals in a set of given intervals.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS 303E

#  Unique Number: Morning (50860)

#  Date Created: 4/17/16

#  Date Last Modified: 4/20/16

#Function to check if any intervals in list overlap
def overlap(lst):

    if len(lst) < 2:
        return False
    else:
        for i in range(len(lst)-2):
            if (lst[i][1] >= lst[i+1][0]):
                return True   
        return False
    
    
#Function to collapse overlapping intervals in list
def collapse(L):
    
    collapsed = []
    
    i = 0
    while i <= len(L)-2:
        if L[i][1] >= L[i+1][0]:
            if L[i][1] <= L[i+1][1]:
                new_tup = (L[i][0], L[i+1][1])
                collapsed.append(new_tup)
                i += 2
            else:
                new_tup = L[i]
                collapsed.append(new_tup)
                i += 2
        else:
            new_tup = L[i]
            collapsed.append(new_tup)
            i += 1
        
        if i == len(L)-1:
            new_tup = L[-1]
            collapsed.append(new_tup)
    if len(L) ==1:
        return L
    return (collapsed)


#Function to order collapsed list by size of intervals
def orderList(col_fin):
    
    size_list = []
    for ele in col_fin:
        diff = ele[1] - ele[0]
        size_list.append(diff)
    
    size_list.sort()

    col_final = []

    for size in size_list:
        for tup in col_fin:
            diff = tup[1] - tup[0]
            if diff == size:
                col_final.append(tup)
    
    return col_final


def main():

    #Open file for reading
    inFile = open("intervals.txt", "r")
    
    #Convert each given interval into tuples, and make a sorted list of them
    interval_list = []
    
    for line in inFile:
        line = line.strip()
        line = line.split()
        interval = []
        for ele in line:
            interval.append(int(ele))
        interval_list.append(tuple(interval))
        
    interval_list.sort()
    
    #Create copy of interval list
    interval_LIST = interval_list[:]
    
    #Check to see if list of intervals contains any overlapping intervals
    is_oLap = overlap(interval_list)
    
    #Collapse interval list until there are no more intersecting intervals
    if is_oLap == True:

        while collapse(interval_LIST) != interval_LIST:
            interval_LIST = collapse(interval_LIST)
    
        col_fin = interval_LIST
    
    else:
        col_fin = interval_LIST
    
    #Call function to order intervals by size
    final_coll = orderList(col_fin)

    #Print statement   
    print ("\nNon-intersecting intervals:")
    
    for tup in final_coll:
        print (tup)
    
    print()
    
    #Close file   
    inFile.close()
    
main()