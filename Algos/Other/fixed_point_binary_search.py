def fixed_point_iterative(A):
    for i in range(len(A)):  # O(n)
        if i == A[i]:
            return i
    return None


A = [0, 11, 12, 3, 41, 12, 14, 16, 18, 21, 24, 27, 34, 44, 46, 49, 55, 66, 78, 87, 89, 90]
target = 23


# print (fixed_point_iterative(A))

def fixed_point(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if mid < A[mid]:
            high = mid - 1
        elif mid > A[mid]:
            low = mid + 1
        else:
            return A[mid]
    return False


# B = [212, 11, 12, 3, 41, 12, 14, 16, 18, 21, 24, 27, 34, 44, 46, 49, 55, 66, 78, 87, 89, 90]
# target = 23
# A = [0,2,5,7,8]
A = [-10,-5,0,3,8]

print(fixed_point(A))
