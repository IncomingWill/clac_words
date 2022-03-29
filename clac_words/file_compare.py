# Title: File Analysis Program
# Program created by William Schaeffer
# CPS 313
# P. 518, Exercise 6, Clac Words Program
# 03.01.22

# This program will read and compare with set methods the contents of two text files
    # Will display lists of: 
        # words that appear in both files - union 
        # words that appear in first file but not second file - difference of sets
        # words that appear in second file but not first - difference of sets 
        # words that appear in either the first or second file but not both - more symmetric difference

# imports for functions

import file_func, sys

# Main Function

def main():
    
    #file_one = open('text1.txt', 'r')              # open text1.txt and text2.txt for testing
    #file_two = open('text2.txt', 'r')
    
    file_one = open(sys.argv[1], 'r')               # open text1.txt and text2.txt from command line                 
    file_two = open(sys.argv[2], 'r')

    file_one_list = []
    file_two_list = []

    file_one_list = file_func.form_word_list(file_one, file_one_list)
    file_two_list = file_func.form_word_list(file_two, file_two_list)

    # for testing
    #print('file one: ', file_one_list)
    #print('file two: ', file_two_list)
   
    set_one = set(file_one_list)                    # create sets for comparisons
    set_two = set(file_two_list)

    print('These are the words that appear in both files:', '\n')
    print(set_one.intersection(set_two), '\n')

    print('These are the words that appear in the first file, but not the second file:', '\n')
    print(set_one.difference(set_two), '\n')

    print('These are the words that appear in the second file, but not the first file:', '\n')
    print(set_two.difference(set_one), '\n')

    print('These are the words that appear in the first file or the second file, but do not appear in both files:', '\n')
    print(set_one.symmetric_difference(set_two), '\n')

    file_one.close                                  # close text1.txt and text2.txt
    file_two.close

main()                                              # call main function

