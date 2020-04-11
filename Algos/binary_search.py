data = [12,213,123,45,45,7,67,564,645,54,3,345,45,534,345,43,65,678,87,0,9,543,21,21,32,45,6,76,87,98,76,4,324,67,900,9]
target = 324

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

def binary_iterative(data, target):
    low = 0
    high = len(data) - 1
    print (low, high)
    while low <= high:
        mid = (high + low) //2
        if target == data[mid]:
            return True
        elif data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
    return False

def binary_recursive(data, target, low, high):
    if low > high:
        return None
    else:
        mid = (high + low) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_recursive(data, target, low, mid - 1)
        elif target > data[mid]:
            return binary_recursive(data, target, mid + 1, high)





# print (binary_iterative(data, 900))
print (binary_recursive(data, 900, 0 , 36))
# print(linear_search(data, target))
