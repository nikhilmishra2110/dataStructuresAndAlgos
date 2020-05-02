from collections import Counter
from functools import reduce

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reverseString(self, s):
        """Two Pointers Approach
            In this approach, two pointers are used to process two array elements at the same time. Usual implementation
             is to set one pointer in the beginning and one at the end and then to move them until they both meet.
            Sometimes one needs to generalize this approach in order to use three pointers, like for classical Sort
            Colors problem.
            Algorithm
            Set pointer left at index 0, and pointer right at index n - 1, where n is a number of elements in the array.
            While left < right:
            Swap s[left] and s[right].
            Move left pointer one step right, and right pointer one step left."""
        r = list(s)
        i = 0
        j = len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1
        return ''.join(r)

    def reverseRecursive(self, s):
        """Recursion, In-Place, \mathcal{O}(N)O(N) Space
                   Does in-place mean constant space complexity?
                   The tricky part is that space is used by many actors, not only by data structures.
                    The classical example is to use recursive function without any auxiliary data structures.
                   Is it in-place? Yes.
                   Is it constant space? No, because of recursion stack.
        """
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l // 2:]) + self.reverseString(s[:l // 2])

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def single_number(self, nums):
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for key, val in d.items():
            if val == 1:
                return key

    def single_number2(self, nums):
        res = 1
        for i in nums:
            res = res ^ i
            print("res==", res)
        return res

    def reverse_linked_list(self, head):
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def move_zeros_to_end(self, nums):
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        while count < n:
            nums[count] = 0
            count += 1
        return nums

    def move_zeros_to_beginning(self, nums):
        n = len(nums)
        read_pointer = n - 1
        write_pointer = n - 1
        while (read_pointer >= 0):
            if nums[read_pointer] != 0:
                nums[write_pointer] = nums[read_pointer]
                write_pointer -= 1
            read_pointer -= 1

        while (write_pointer >= 0):
            nums[write_pointer] = 0
            write_pointer -= 1
        return nums

    def majority_element(self, nums):
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) +1

        for key, value in d.items():
            if value > len(nums)//2:
                return key

    def sorted_array_to_bst(self, nums):
        if len(nums) ==0:
            return
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sorted_array_to_bst(nums[:mid])
        root.right = self.sorted_array_to_bst(nums[mid+1:])  # do not forget +1
        return root

    def isAnagram(self, s, t):
        print (s,t)
        l1 = list(s)
        l2 = list(t)
        l1.sort()
        l2.sort()
        return l1==l2


    def maxProfit(self, prices):
        max_sum = prices[0]
        current_sum = max_sum
        for i in range(1,len(prices)):
            current_sum = max(prices[i], current_sum+prices[i])
            print ("Current sum = ", current_sum)
            max_sum = max(current_sum, max_sum)
        return max_sum

    def max_profit2(self,prices):
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

    def containsDuplicate(self, nums):
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1

        for key, value in d.items():
            if value > 1:
                return True
        return False



    def romanToInt(self, s):
        roman = {
                    'M': 1000,
                    'D': 500 ,
                    'C': 100,
                    'L': 50,
                    'X': 10,
                    'V': 5,
                    'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
            print ("z - ", z)
            print ("roman[s[i]] - ", roman[s[i]])
        return z + roman[s[-1]]


    def ExcelColumns(self, s):
        return reduce(lambda x, y: x * 26 + y, [ord(c) - 64 for c in list(s)])


    def titleToNumber(self, s):
        """
        https://leetcode.com/problems/excel-sheet-column-number/discuss/52154/Concise-java-solution-with-explanation.
        """
        res = 0
        for i in s:
            print("ord(i) -> ",ord(i))
            print("ord(A) -> ",ord("A"))
            print("ord(i) - ord(A) -> ",ord(i) - ord("A"))
            res = res * 26 + ord(i) - ord('A') + 1
            print("res is ", res)
        return res

    def mergeTwoLists1(self, l1, l2):
        tmp = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return tmp.next

    def mergeTwoLists2(self, l1, l2):
        '''
        https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).
        '''
        curr = ListNode(0)
        while (l1 and l2):
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return curr


    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        index = -1
        for i in range(len(s)):
            if d[s[i]] == 1:
                index = i
                break
        return index

    def pascals_triangle(self, numRows):
        # this is the list of list
        triangle = []

        # edge case check
        if numRows == 0:
            return triangle

        # just the first row
        first_row = []
        first_row.append(1)
        triangle.append(first_row)

        # for all rows
        for i in range(1, numRows):
            # get the whole  previous row and
            prev_row = triangle[i-1]
            # building the actual row
            row = []
            # One at the beginning
            row.append(1)
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])

            # One at the end
            row.append(1)
            triangle.append(row)
        return triangle

    def missingNumber(self, nums):
        actual_sum = sum(nums)
        n = len(nums)+1 # since we knw there is one missing, adding one
        return n*(n-1)/2 -actual_sum

    def intersect(self, nums1 , nums2):
        d = {}
        res = []
        for i in nums1:
            d[i] = d.get(i,0)+1

        for i in nums2:
            if i in d and d[i] > 0:
                res.append(i)
                d[i]-=1
        return res



#1001209191712094
s = Solution()
# print(s.reverseString("Nikhil"))
# print(s.reverseRecursive("Nikhil"))
# print (s.single_number2([4,4,2, 2,1]))
# print (s.move_zeros_to_end([1,2,0,9,8,0,9,8,7,6,90,0,0,0,1,1,1,1,1]))
# print(s.move_zeros_to_beginning([1, 10, 20, 0, 59, 63, 0, 88, 0]))
# print(s.majority_element([1, 20, 20]))
# print(s.sorted_array_to_bst([1, 2, 5,6,9,12,14,16,18,21,24,26]))
# print (s.isAnagram("nikhil", "mishra"))
# print (s.isAnagram("oto", "oto"))
# print (s.max_profit2([7,1,5,3,6,4]))
# print (s.containsDuplicate([1,2,3,4,5,1]))
# print (s.romanToInt('III'))
# print (s.romanToInt('LVIII'))
# print (s.ExcelColumns("AB"))
# print(s.titleToNumber("ZA"))
# print(s.titleToNumber("AC"))
# print(s.titleToNumber("AD"))
# print(s.titleToNumber("AE"))
# print (s.pascals_triangle(5))
# print (s.missingNumber([]))
print (s.intersect([1,2,2,1], [2]))