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
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
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
        if sequence[seq_idx] == array[arr_idx]:
            seq_idx += 1
        arr_idx += 1
    return seq_idx == len(sequence)


"""
    
# Implement a BST:
    Recursive implementation:
        Avg. Case (Search Insert and delete):
            Time: O(log(N))
            Space: O(log(N))
        Worst case:
            Time: O(N)
            Space: O(N)
            
    Iterative implementation:
        Avg. Case:
            Time: O(log(N))
            Space: O(1)
        Worst case:
            Time: O(N)
            Space: O(1)
            
    Iterative is good from space point of view as you will not be storing frames on the call stack.
"""


class BST:
    def __init__(self, data):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
        =================================================
         Avg case: Time: O(log(N)) | Space: O(1) is because we implement iteratively
         Worst case: Time: O(N) | Space: O(1)
        =================================================
         Approach:
            Take a currentNode
                compare value
                    if less then left subtree - if data absent on left insert otherwise keep exploring right
                    elif value greater then check right  subtree - if data absent on right insert otherwise keep exploring
                     right
        """
        currentNode = self
        while True:
            if value < currentNode.value:  # Explore the left tree
                if currentNode.left is None:  # If there is no left node
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left  # value not found, keep exploring the left subtree
            else:  # Explore the right tree
                if currentNode.right is None:  # there is no right value
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right  # value not found, keep exploring the right subtree
        return self  # for doing testBST.insert(5).insert(6) ....not relevant

    def contains(self, value):
        """
        =================================================
         Avg case: Time: O(log(N)) | Space: O(1) is because we implement iteratively
         Worst case: Time: O(N) | Space: O(1)
        =================================================
        Approach:
            take currentNode:
                check value:
                    3 cases >, <, ==
                    if >:
                        check right
                    elif <:
                        check left
                    else:
                        value found - return true

        """
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    def remove(self, value, parent_node=None):
        """
        =================================================
         Avg case: Time: O(log(N)) | Space: O(1) is because we implement iteratively
         Worst case: Time: O(N) | Space: O(1)
        =================================================
        Approach:
            It is a two step process. First find the value and then delete.
            Find in left or right subtree
            if fpund:
                if current node is two non-null children curr.left is not None and curr.right is not none: get min from
                    curr.right.getMinValue() -smallest leftmost value of right subtree -
                else

        """
        curr = self
        while curr is not None:
            if value < curr.value:  # find the value
                parent_node = curr
                curr = curr.left
            elif value > curr.value:  # find the value
                parent_node = curr
                parent_node = curr.right
            else:  # found the value
                if curr.left is not None and curr.right is not None:  # the node has two non-null childrenf
                    #         5
                    #       /  \
                    #      3    7
                    #    /      \
                    #   0        9
                    curr.value = curr.right.getMinValue()  # fetch the min from right tree and replace the curr value with it
                    curr.right.remove(curr.value, curr)  # remove the value- minimum value from the right subtree
                elif parent_node is None:  # we need to delete root node
                    if curr.left is not None:  # one of the child is missing here left is missing
                        #     5
                        #   /
                        # 3
                        #
                        #
                        curr.value = curr.left.value
                        curr.right = curr.left.right
                        curr.left = curr.left.left  # Assign the left value last so that we do not change it b4 using it
                    elif curr.right is not None:  # one of the child is missing here right is missing
                        #     5
                        #      \
                        #      9
                        #
                        #
                        curr.value = curr.right.value
                        curr.left = curr.right.left
                        curr.right = curr.right.right
                    else:  # here we have root node and no children at all
                        curr.value = None
                        #     5
                        #

                elif curr == parent_node.left:  # Check if current node is left child itself
                    parent_node.left = curr.left if curr.left is not None else curr.right
                    #     5
                    #   /
                    # 3
                    #  \
                    #   4
                elif curr == parent_node.right:
                    curr.right = curr.left if curr.left is not None else curr.right
                    #     5
                    #       \
                    #       8
                    #      /
                    #    6
                    #
                break
            return self

    def getMinValue(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.value
