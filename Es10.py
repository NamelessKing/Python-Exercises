# coding=utf-8
'''

Define a function overlapping() that takes two lists and returns True
if they have at least one member in common, False otherwise.
You may use your is_member() function, or the in operator,
but for the sake of the exercise, you should (also)
write it using two nested for-loops.


'''

#FIRST SOLUTION
def overlapping(listA,listB):

    control = False

    for i in listA:

        if not control and i in listB:
            control = True

    return control

a = [1,2,3,4,5,6]
b = [7,8,9,10,1]

print overlapping(a,b)



#SECOND SOLUTION
def _overlapping(listA,listB):

    control = False

    for i in listA:
        for j in listB:

            if i == j:
                control = True

    return control

a = [1,2,3,4,5,6]
b = [7,8,9,10,1]

print _overlapping(a,b)
