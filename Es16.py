# coding=utf-8
'''

Write a function filter_long_words() that takes a list of words and an
integer n and returns the list of words that are longer than n.

'''


def long_words(n,list):

    l = []

    for i in list:

        if len(i) > n:
            l.append(i)

    return l


print long_words(4,['ciao','hello','baby','goodnight'])