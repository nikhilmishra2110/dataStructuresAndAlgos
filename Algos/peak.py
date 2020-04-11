def peak_iterative(A):
    for i in range(len(A)):
        if A[i] > A[i+1] and A[i-1] < A[i]:
            return A[i]

    return None

# A = [1,2,3,4,5,4,3,2,1]
A = [1,6,4,3,2,1]

# TODO: worst case is [1,2,3,4,5,6,7,9.................9999999999, 1]
print (peak_iterative(A))