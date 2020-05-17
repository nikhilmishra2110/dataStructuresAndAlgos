# O(n^2) time and O(1) space
def twoNumberSum1(array, targetSum):
    # Brute force two for loop to find the sum
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


# O(n) time | O(n) space
def twoNumberSum2(array, targetSum):
    # Hashtable
    nums = {}
    for num in array:
        compliment = targetSum - num
        if compliment in nums:
            return [compliment, num]
        else:
            nums[num] = True
    return []

# O(nlog) time | O(1) space
def twoNumberSum3(array, targetSum):
    # First sort the array and this takes O(NlogN)
    # two pointer and sort
    array.sort()
    left = 0
    right = len(array)-1
    while left< right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [ array[left], array[right]]
        elif currentSum < targetSum:
            left+=1
        elif currentSum > targetSum:
            right-=1
    return []


def isSubsequence(array, sequence):
    """
    Approach:
    We will have to traverse both arrays as we need to exhaustively find all the elements of subsequence in primary
    array.
    We can use a while loop and use two pointers for our arrays. As soon as we find sequence element in array
    we will update pointers
    """
    seq_idx = 0
    arr_idx = 0

    while seq_idx < len(sequence) and arr_idx < len(array):
        if sequence[seq_idx]== array[arr_idx]:
            seq_idx+=1
        arr_idx+=1
    return seq_idx == len(sequence)


