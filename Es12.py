# coding=utf-8
'''

Define a procedure histogram() that takes a list of integers and
prints a histogram to the screen. For example,histogram([4, 9, 7]) 
should print the following:

****

*********

*******
'''


#1° SOLUTION
def histogram(list):

    for i in list:

        s = ''
        for i in range(i):
            s += '*'

        print s+'\n'

    return

histogram([4,9,7])



#1° SOLUTION
def _histogram(list):

    for i in list:
        print '*'*i

    return


_histogram([4,9,7])
