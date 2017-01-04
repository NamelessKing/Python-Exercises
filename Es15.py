# coding=utf-8
'''

Write a function find_longest_word() that takes a list of words and
returns the length of the longest one.

'''

def longest_word(list):

    max = len(list[0])

    for i in list:

        if len(i) > max:
            max = len(i)

    return max


print longest_word(['ciao','hello','baby','goodnight'])