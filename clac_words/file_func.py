# Title: File Analysis Program Functions
# Program created by William Schaeffer
# CPS 313
# P. 518, Exercise 6, Clac Words Program
# 03.01.22

# Function to create list of words from a .txt file
    # while fileInput is not an empty string, split the sentence into a list

def form_word_list(text, list):

    punctuation = ",."                                                  # to remove punctuation

    fileInput = text.readline().lower()                                 # read line, convert to lowercase
    for element in punctuation:                                         # replace periods and commas with ""
        fileInput = fileInput.replace(element, "")
    list.append(fileInput.split())                                      # split string into list, add to list

    while fileInput != '':

        fileInput = text.readline().lower()                             # read the next line
        for element in punctuation:                                     # remove periods and commas
            fileInput = fileInput.replace(element, "")

        list.append(fileInput.split())

    list = sum(list, [])                    # consolidate list of lists to one list

    return list
