


#Define a function max_of_three() that takes three numbers as
#arguments and returns the largest of them.




def max_of_three(a,b,c):

    max=0
    if a > b:
        max = a
    else:
        max = b

    if max > c :
        return max
    else:
        return c



print max(234,124,43)


def max_of_three2(a, b, c):
    if a > b and a > c:
        print a
    elif b > c:
        print b
    else:
        print c


print max_of_three2(0, 15, 2)