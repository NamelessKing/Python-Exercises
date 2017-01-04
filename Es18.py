# coding=utf-8
'''

A pangram is a sentence that contains all the letters of the English
alphabet at least once, for example: The quick brown fox jumps over
the lazy dog. Your task here is to write a function to check a sentence
to see if it is a pangram or not.

'''

#First Solution
def is_pangram(string):

    alphabet_list = []
    num_of_alphabets = 26

    for i in string:

        if i.isalpha() and i.lower() not in alphabet_list:
            alphabet_list.append(i.lower())

    return len(alphabet_list) == num_of_alphabets


print is_pangram("How vexingly quick daft zebras jump!" )




#Second Solution
def isPangram(string):

    pangram = False

    for i in ("abcdefghijklmnopqrstuvwxyz"):

        if i not in string.lower()and not pangram:
            pangram = True

    return not pangram


print isPangram("Bright vixens jump; dozy fowl quack." )
