# coding=utf-8
'''

Define a function is_palindrome() that recognizes palindromes
(i.e. words that look the same written backwards). For example, 
is_palindrome("radar") should return True

'''
#FIRST SOLUTION
def is_palindrome(string):

    i = 0
    j = len(string)-1
    control = False

    while i < j and not control:

        if string[i] == string[j]:

            i += 1
            j -= 1

        else:
            control = True

    return not control


print is_palindrome('radar')


#SECOND SOLUTION

def isPalindrome(string):

    if string == string[::-1]:
        return True
    else:
        return False


print isPalindrome('radar')