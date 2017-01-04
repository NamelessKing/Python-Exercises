# coding=utf-8
'''

Write a program that maps a list of words into a list of integers
representing the lengths of the correponding words.


'''


def maps_list_of_words(list):

    l = []

    for i in list:
        l.append(len(i))

    return l


print maps_list_of_words(['ciao','hello','baby','goodnight'])
