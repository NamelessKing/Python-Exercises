# coding=utf-8
'''

Define a function reverse() that computes the reversal of a string. For example,
reverse("I am testing") should return the string "gnitset ma I".

'''

#FIRST SOLUTION

def reverse(string):

    reversed = ''
    for i in range(len(string))[::-1]:
        reversed += string[i]
    return reversed

print reverse('I am testing')




#SECOND SOLUTION

def _reverse(string):

    reversed = []
    for i in range(len(string))[::-1]:
        reversed.append(string[i])
    reversed = ''.join(reversed)
    return reversed

print _reverse('I am testing')