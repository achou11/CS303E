#  File: Grid.py

#  Description: This program finds the greatest product of four adjacent numbers in a grid.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS 303E

#  Unique Number: Morning (50860)

#  Date Created: 4/14/16

#  Date Last Modified: 4/15/16

#Function to calculate greatest product of 4 numbers in a row
def prod_rows(r):
    prod = 1
    prod_max = 0
    
    for i in range(len(r)):
        for j in range(len(r[i]) - 3):
            prod = r[i][j] * r[i][j+1] * r[i][j+2] * r[i][j+3]
            if prod_max < prod:
                prod_max = prod
    
    return prod_max


#Function to calculate greatest product of 4 numbers in a column
def prod_cols(c):
    prod = 1
    prod_max = 0
    
    for i in range(len(c)):
        for j in range(len(c[i]) - 3):
            prod = c[j][i] * c[j+1][i] * c[j+2][i] * c[j+3][i]
            if prod_max < prod:
                prod_max = prod
    
    return prod_max

#Function to calculate greatest product of diagonal going right to left
def diProd_rl (a):
	prod = 1
	prod_max = 0
	for i in range (len(a) - 3):
		for j in range (len(a[i]) - 3):
			prod = a[i][j] * a[i + 1][j + 1] * a[i + 2][j + 2] * a[i + 3][j + 3]
			if prod_max < prod:
				prod_max = prod
	return prod_max


#Function to calculate greatest product of diagonal going left to right
def diProd_lr (b):
	prod = 1
	prod_max = 0
	for i in range (len(b)):
		for j in range (len(b[i]) - 3):
			prod = b[i][j] * b[i - 1][j + 1] * b[i - 2][j + 2] * b[i - 3][j + 3]
			if prod_max < prod:
				prod_max = prod
	return prod_max



def main():
    
    #Open fie for reading
    inFile = open ("grid.txt", "r")
    
    #Read first line to get dimensions of grid
    dim = inFile.readline()
    dim = dim.strip()
    dim = int(dim)
    
    #create empty grid and populate it
    grid = []
    for i in range(dim):
        row = inFile.readline()
        row = row.strip()
        row = row.split()
        for j in range(dim):
            row[j]  = int(row[j])
        grid.append(row)

    #Variables containing max products
    
    max_diRL = diProd_rl(grid)
    
    max_diLR = diProd_lr(grid)
    
    max_rows = prod_rows(grid)
    
    max_cols = prod_cols(grid)

    #Create list of the max values and print out max within list
    
    max_list = []
    
    max_list.append(max_diRL)
    max_list.append(max_diLR)
    max_list.append(max_rows)
    max_list.append(max_cols)
    
    #Print statement
    print ("The greatest product is " + str(max(max_list)) + ".")

    #Close file
    inFile.close()
    
main()
        