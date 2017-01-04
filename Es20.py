# coding=utf-8
'''
Represent a small bilingual lexicon as a Python dictionary in the
following fashion {"merry":"god", "christmas":"jul", "and":"och",
"happy":gott", "new":"nytt", "year":"ar"} and use it to translate
your Christmas cards from English into Swedish. That is, write a
function translate() that takes a list of English words and returns
a list of Swedish words.


'''

def translate(string):

    l = []
    s = ""
    dictionarie = { "merry" :"god",
                    "christmas" :"jul",
                    "and" :"och",
                    "happy" :"gott",
                    "new" :"nytt",
                    "year" :"ar"}

    l = string.split(" ")

    for i in l:

        if i in dictionarie:
            s += dictionarie[i]+" "

    return s


print translate("merry christmas and new year happy")