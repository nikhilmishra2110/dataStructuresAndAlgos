from sys import maxsize


def createStack():
    stack = []
    return stack

def push(stack, data):
    stack.append(data)

def isEmpty( stack):
    return len(stack) ==0

def pop( stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack.pop()

def peek( stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)  # return minus infinite
    return stack[len(stack) - 1]



stack = createStack()
push(stack, 10)
push(stack,20)
push(stack, 30)
print(pop(stack),  " popped from stack")