#  File: DNA.py

#  Description: This program reads a text file containing two DNA strings and returns the longest common string of characters for them.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS 303E

#  Unique Number: Morning (50860)

#  Date Created: 3/22/16

#  Date Last Modified: 3/25/16


#Create function that breaks string into all of its possible substrings
def substr(st_shorter, st_longer):
    
    wnd = len(st_shorter)
    
    max_len = 0
    first_str = ""
    
    list_substr = []
    while (wnd > 0):
        start_idx = 0
        while (start_idx + wnd <= len(st_shorter)):
            sub_strand = st_shorter[start_idx : start_idx + wnd]
            
            if (st_longer.find(sub_strand) > -1):
                if (max_len <= len(sub_strand)):
                    max_len = len(sub_strand)
                    print (first_str + sub_strand)
                    first_str = "       "
            start_idx += 1
            
        wnd = wnd - 1
    
    if max_len == 0:
        print ("No Common Sequence Found")
        
def main():
    
    print()
    
    print ("Longest Common Sequences \n")
    
    #open file for reading
    dna_file = open ("dna.txt", "r")
    
    #identify number of pairs in the file
    pair_count = dna_file.readline()
    pair_count = pair_count.strip()
    pair_count = int (pair_count)
    
    #read each pair of DNA strands
    for i in range (pair_count):
        strand_1 = dna_file.readline()
        strand_2 = dna_file.readline()
        
    #remove white space from either end
        str1_strip = strand_1.strip()
        str2_strip = strand_2.strip()
     
    #make each strand upper case   
        str1_upper = str1_strip.upper()
        str2_upper = str2_strip.upper()
    
    #order strands by size
        if (len(str1_upper) > len(str2_upper)):
            dna_long = str1_upper
            dna_short = str2_upper
        else:
            dna_long = str2_upper
            dna_short = str1_upper
    
    #call function to check which substrings in the shorter strand are in the longer strand
        print ("Pair" + str(i + 1) + ": ", end = "")
        
        substr_short = substr(dna_short, dna_long)
    
        print()

            
    #close file
    dna_file.close()

main()