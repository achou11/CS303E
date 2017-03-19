# Books.py

# Description: Program conducts frequency analysis on two books.

# Student Name: Andrew Chou

# Student UT EID: aoc349

# Course Name: CS 303E

# Unique Number: Morning (50860)

# Date Created: 4/22/16

# Date Last Modified: 4/27/16

# Function to create comprehensive word list
def create_word_dict(word_dict):
    wordFile = open("./words.txt", "r")
    for word in wordFile:
        word = word.strip()
        word_dict[word] = 1

    return word_dict
  
    wordFile.close()
  
    
# Remove punctuation marks and digits
def parseString (st):
    s = ''
    for ch in st:
        if ch.isalpha() == True or ch.isspace() == True:
            s += ch
        elif ch == "'":
            s += ch
        else:
            s += ' '
    
    s = s.replace("'s", " ")
    s = s.replace("' ", " " )
    
    return s

# Function to get the frequency of words used in book
def getWordFreq(book, universal):
    
    # Create dictionary for all words found in a book
    book_dict = {}
    
    # Go through lines of book file and convert each into list of words
    
    for line in book:
        line = line.strip()
        line = parseString(line)
        word_list = line.split()

        # Check if each word belongs to global dictionary
        
        for word in word_list:
            
            # Add word to book dictionary 
            if word[0].isupper():
                if word.lower() in universal:
                    wordLow = word.lower()
                    
                    if wordLow in book_dict:
                        book_dict[wordLow] += 1
                    else:
                        book_dict[wordLow] = 1
            
            if word in universal:
                if word in book_dict:
                    book_dict[word] += 1
                else:
                    book_dict[word] = 1
    
    # Create dictionary for frequency of words in a book
    freq_dict = {}
    
    # Update frequencies of words in the book
    for word in book_dict:
        freq = book_dict[word]
        
        if freq in freq_dict:
            (freq_dict[freq]).append(word)
        else:
            new_list = []
            new_list.append(word)
            freq_dict[freq] = new_list
    

    return freq_dict, book_dict


# Function to compare two novels based on word frequency analyses
def wordComparison(author1, freq1, author2, freq2, book1, book2):

    # Assign number of distinct words to two variables
    num_distinct1 = len(freq1)
    num_distinct2 = len(freq2)

    # Initialize two variables for total distinct words, set of distinct words, total words for both books
    total_distinct1 = 0
    total_distinct2 = 0
    distinct1 = []
    distinct2 = []
    total1 = 0
    total2 = 0

    for key1 in freq1:
        total_distinct1 += len(freq1[key1])
        for word1 in freq1[key1]:
            distinct1.append(word1)

    for key2 in freq2:
        total_distinct2 += len(freq2[key2])
        for word2 in freq2[key2]:
            distinct2.append(word2)

    # Add to count of total words variables
    for i in freq1:
        total1 += len(freq1[i]) * i
    for i in freq2:
        total2 += len(freq2[i]) * i
    
    # Obtain set of distinct words used by one author but not the other
    difference1 = set(distinct1) - set(distinct2)
    difference2 = set(distinct2) - set(distinct1)

    count_first_author = len(difference1)
    count_second_author = len(difference2)
    
    # Get total frequency of words in unique sets
    freq_distinct1 = 0
    freq_distinct2 = 0
    
    for word1 in difference1:
        freq_distinct1 += book1[word1]
    
    for word2 in difference2:
        freq_distinct2 += book2[word2]
    
    rel_freq1 = round(freq_distinct1 / total1 * 100, 10)
    rel_freq2 = round(freq_distinct2 / total2 * 100, 10)
    
    # Print Statements
    print(author1)
    print("Total distinct words =", total_distinct1)
    print("Total words (including duplicates) =", total1)
    print("Ratio (% of total distinct words to total words) =", str(total_distinct1 / total1 * 100))
    
    print()
    
    print(author2)
    print("Total distinct words = ", str(total_distinct2))
    print("Total words (including duplicates) = " + str(total2))
    print("Ratio (% of total distinct words to total words) = " + str(total_distinct2 / total2 * 100))
    
    print("\n" + author1 + " used " + str(count_first_author) + " words that " + author2 + " did not use.")
    print("Relative frequency of words used by " + author1 + " not in common with " + author2 + " = " + str(rel_freq1))
    
    print("\n" + author2 + " used " + str(count_second_author) + " words that " + author1 + " did not use.")
    print("Relative frequency of words used by " + author2 + " not in common with " + author1 + " = " + str(rel_freq2))

    print()
    
    
def main():
    
    # Create word dictionary from comprehensive word list
    word_dict = {}
    create_word_dict(word_dict)

    # Enter names of the two books in electronic form
    book1 = input("Enter name of first book: ")
    book2 = input("Enter name of second book: ")
    print()
      
    # Enter names of the two authors
    author1 = input("Enter last name of first author: ")
    author2 = input("Enter last name of second author: ")
    print()
    
    # Open book files for reading
    book1 = open(book1, "r")
    book2 = open(book2, "r")
    
    # Get the frequency of words used by the two authors
    wordFreq1, book_dict1 = getWordFreq (book1, word_dict)
    wordFreq2, book_dict2 = getWordFreq (book2, word_dict)
  
    # Compare the relative frequency of uncommon words used by the two authors
    wordComparison (author1, wordFreq1, author2, wordFreq2, book_dict1, book_dict2)
    
    #close books
    book1.close()
    book2.close()
    
    
main()