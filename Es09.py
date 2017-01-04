# coding=utf-8
'''

Write a function is_member() that takes a value (i.e. a number, string,
etc) x and a list of values a, and returns True if x is a member of a,
False otherwise. (Note that this is exactly what the in operator does,
but for the sake of the exercise you should pretend
Python did not have this operator.)


'''
#FIRST SOLUTION
def is_member(x,list):

    for i in list:

        if x == i:
            return True

    return False


print is_member('ciao',[2,'ciao',5,6])



#SECOND SOLUTION

def isMember(x,list):

    if x in list:
        return True
    else:
        return False

print isMember('ciao',[2,'ciao',5,6])