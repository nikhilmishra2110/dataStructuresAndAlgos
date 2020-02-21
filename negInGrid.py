from bisect import *


def countNegatives(self, A):
    return sum(a < 0 for r in A for a in r)

def countNegatives2(self, A):
    return sum(bisect_left(type('', (), {'__getitem__': lambda _, i: r[~i]})(), 0, 0, len(r)) for r in A)


li = [1, 3, 4, 4, 4, 6, 7]

#using bisect() to find index to insert new element
print(bisect(li, 4))
print("The leftmost index to insert, so list remains sorted is  : ", end="")
print(bisect_left(li, 4))
print("The rightmost index to insert, so list remains sorted is  : ", end="")
print(bisect_right(li, 4, 0, 4))


