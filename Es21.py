# coding=utf-8
'''
Write a function char_freq() that takes a string and builds a frequency
listing of the characters contained in it. Represent the frequency
listing as a Python dictionary. Try it with something
like char_freq("abbabcbdbabdbdbabababcbcbab").


'''
#First Solution
def char_freq(string):

    apha_list = []
    freq_list = {}

    for i in string:

        if i not in apha_list:
            apha_list.append(i)

    for i in apha_list:
        count = 0
        for j in string:
            if i == j:
                count += 1
        freq_list[i] = count

    return  freq_list




print char_freq("ciao come stai una domanda che non faccio mai")




#Second Solution
def charFreq(string):

    freq_list = {}

    for i in string:
        freq_list[i] = freq_list.get(i,0)+1

    return freq_list




print charFreq("abcdeff")















