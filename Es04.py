# coding=utf-8
'''

Write a function that takes a character (i.e. a string of
length 1) and returns True if it is a vowel, False otherwise

'''

def isVowel(character):

    vowel = 'aeiou'

    for i in vowel:
        if i == character:
            return True
    return False

print isVowel('b')

print isVowel('a')


'''

another solution

'''

def is_vowel(character):

    if character in ('aeiou'):
        return True
    return False

print is_vowel('a')

print is_vowel('x')