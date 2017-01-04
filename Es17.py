'''

Write a version of a palindrome recognizer that also accepts phrase
palindromes such as "Go hang a salami I'm a lasagna hog.",
"Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir",
or the exclamation "Dammit, I'm mad!". Note that punctuation,
capitalization, and spacing are usually ignored.

'''


#FIRST SOLUTION
def is_palindrome(string):
    ignored_case = ['\'', ' ', '.', '?', ',', '!', '\"']
    palindrome_string = ''
    palindrome = False

    i = 0
    j = len(string) - 1

    for i in string:

        if i not in ignored_case:
            palindrome_string += i.lower()

    i = 0
    j = len(palindrome_string) - 1
    while i < j and not palindrome:

        if palindrome_string[i] == palindrome_string[j]:
            i += 1
            j -= 1
        else:
            palindrome = True

    return not palindrome


print is_palindrome("Dammit, I'm mad!")



#SECOND SOLUTION
def isPalindrome(string):
    ignored_case = ['\'', ' ', '.', '?', ',', '!', '\"']
    palindrome_string = ''
    palindrome = False

    i = 0
    j = len(string) - 1

    for i in string:

        if i not in ignored_case:
            palindrome_string += i.lower()

    if palindrome_string == palindrome_string[::-1]:
        palindrome = True
    else:
        palindrome = False

    return palindrome


print isPalindrome("Dammit, I'm mad!")




#THIRD SOLUTION
def _isPalindrome(string):

    palindrome_string = ''
    palindrome = False

    for i in string:
        if i.isalpha():
            palindrome_string += i.lower()


    if palindrome_string == palindrome_string[::-1]:
        palindrome = True
    else:
        palindrome = False

    return palindrome


print _isPalindrome("Dammit, I'm mad!")


















