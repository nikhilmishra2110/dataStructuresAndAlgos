from Algos.Other.stack import Stack

def reverse_string(input_string):
    s = Stack()

    '''Loop to push the items into the stack'''
    for i in range(len(input_string)):
        s.push(input_string[i])

    reverse_str = ""
    '''Loop to pop the string in reverse'''
    while not s.is_empty():
        reverse_str += s.pop()

    return reverse_str


n = "This is India"
print(reverse_string(n))