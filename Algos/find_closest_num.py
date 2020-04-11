def find_closest_num(A, target):
    curr_smallest_diff = float("Inf")
    closest_number = None
    low = 0
    high = len(A) - 1

    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:

        mid = (low + high) // 2
        if mid + 1 < len(A):
            smallest_diff_right = abs(A[mid + 1] - target) # there can be negetive numberss
        if mid > 0:
            smallest_diff_left = abs(A[mid - 1] -target)

        if smallest_diff_left < curr_smallest_diff:
            curr_smallest_diff = smallest_diff_left
            closest_number = A[mid -1]

        if smallest_diff_right < curr_smallest_diff:
            curr_smallest_diff = smallest_diff_right
            closest_number = A[mid + 1]

        if target < A[mid]:
            high = mid - 1
        elif target > A[mid]:
            low = mid + 1
        else:
            return A[mid]
    return closest_number


A = [1,3,6,8,9,12,14,16,18,21,24,27,34,44,46,49,55,66,78,87,89,90]
target = 23
print (find_closest_num(A,target))