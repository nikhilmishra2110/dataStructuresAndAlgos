from Algos.Other.stack import Stack

def convert(dec):
    s = Stack()

    while(dec >0):
        remainder = dec %2
        s.push(remainder)
        dec //=2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print (convert())