# coding=utf-8
'''

Define a function that computes the length of a given list
or string. (It is true that Python has the len() function
built in, but writing it yourself is nevertheless a good
exercise.)

'''

def len_of_string(string):

    count = 0
    for i in string:
        count += 1

    return count

print len_of_string("ciao000000")
