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

        r = list(s)  # convert string to list
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
            d[i] = d.get(i, 0) + 1

        for key, value in d.items():
            if value > len(nums) // 2:
                return key

    def sorted_array_to_bst(self, nums):
        if len(nums) == 0:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sorted_array_to_bst(nums[:mid])
        root.right = self.sorted_array_to_bst(nums[mid + 1:])  # do not forget +1
        return root

    def isAnagram(self, s, t):
        print(s, t)
        # convert string to list
        l1 = list(s)
        l2 = list(t)
        l1.sort()
        l2.sort()
        return l1 == l2

    def maxProfitMultipleTx(self, prices):
        """

        :rtype: object
        """
        if not prices or len(prices) is 1:
            return 0

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit

    def maxProfitOneTx(self, prices):
        max_profit, min_price = 0, float('inf')
        for i in prices:
            min_price = min(min_price, i)
            profit = i - min_price
            max_profit = max(max_profit, profit)
        return max_profit

    def containsDuplicate(self, nums):
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        for key, value in d.items():
            if value > 1:
                return True
        return False

    def romanToInt(self, s):
        roman = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
            print("z - ", z)
            print("roman[s[i]] - ", roman[s[i]])
        return z + roman[s[-1]]

    def ExcelColumns(self, s):
        return reduce(lambda x, y: x * 26 + y, [ord(c) - 64 for c in list(s)])

    def titleToNumber(self, s):
        """
        https://leetcode.com/problems/excel-sheet-column-number/discuss/52154/Concise-java-solution-with-explanation.
        """
        res = 0
        for i in s:
            print("ord(i) -> ", ord(i))
            print("ord(A) -> ", ord("A"))
            print("ord(i) - ord(A) -> ", ord(i) - ord("A"))
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
            d[i] = d.get(i, 0) + 1
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
            prev_row = triangle[i - 1]
            # building the actual row
            row = []
            # One at the beginning
            row.append(1)
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])

            # One at the end
            row.append(1)

            # this should be within the for loop because
            triangle.append(row)
        return triangle

    def missingNumber(self, nums):
        actual_sum = sum(nums)
        n = len(nums) + 1  # since we knw there is one missing, adding one
        return n * (n - 1) / 2 - actual_sum

    def intersect(self, nums1, nums2):
        d = {}
        res = []
        for i in nums1:
            d[i] = d.get(i, 0) + 1

        for i in nums2:
            if i in d and d[i] > 0:
                res.append(i)
                d[i] -= 1
        return res

    def isHappy(self, n):
        '''Because if the algorithm sees a number it has seen before, then it follows that it will go on the same path
        and thus see it once again, creating an infinite loop. So a valid solution requires that all numbers seen on
         the way to reducing n to 1 be unique.'''
        s = set()
        while n != 1:
            if n in s: return False
            s.add(n)
            print("s -->>>", s)
            n = sum([int(i) ** 2 for i in str(n)])
            print("n after ", n)
        return True

    def hammingWeight(self, n):
        count = 0
        m = bin(n).count('')
        for i in m:
            if i == '1':
                count += 1
        return count

    def hamming2(self, n):
        return int(bin(n).count('1'))

    def isSymmetric(self, root):
        if not root:
            return True
        return self.checker(root.left, root.right)

    def checker(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        else:
            return node1.val == node2.val and self.checker(node1.left, node2.right) and self.checker(node1.right,
                                                                                                     node2.left)

    def maxSubArray(self, nums):
        # def maxSubArray(self, nums: List?[int]) -> :
        max_sum = curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, num + curr_sum)
            max_sum = max(curr_sum, max_sum)
            print("num -->", num)
            print("curr sum -->", curr_sum)
            print("max sum -->", max_sum)
            print()
        return max_sum

    def twoSum(self, num, target):
        d = {}
        for i in range(len(num)):
            compliment = target - num[i]
            if compliment in d:
                return [d[compliment], i]
            else:
                d[num[i]] = i

    def removeDuplicates(self, nums):
        write_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[write_index]:
                # first increment the counter as this is a new number
                write_index += 1
                nums[write_index] = nums[i]
        return write_index + 1

    def countAndSay(self, n):
        # TODO: fix this
        s = '1'
        for _ in range(n - 1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count) + let
                    let = l
                    count = 1
            temp += str(count) + let
            s = temp
        return s

    def isPalindromeLinkedList(self, head):
        if not head or not head.next: return True

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        while prev:
            if head.val != prev.val: return False
            head = head.next
            prev = prev.next

        return True

    def intersectionLinkedList(self, headA, headB):
        if not headA or not headB: return None

        a_pointer = headA
        b_pointer = headB

        while (a_pointer != b_pointer):
            if not a_pointer:
                a_pointer = headB
            else:
                a_pointer = a_pointer.next

            if not b_pointer:
                b_pointer = headA
            else:
                b_pointer = b_pointer.next

        return a_pointer

    def trailingZeroes(self, n):
        zeros = 0
        while n > 0:
            n //= 5
            zeros += n
        return zeros

    #     10 =  10 9 8 7 6 5 4 3 2 1

    def factorial(self, n):
        if n == 1 or n == 0: return 1
        return n * self.factorial(n - 1)

    def commonprefix(m):
        if not m: return ''
        s1 = min(m)
        s2 = max(m)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1

    def powerOfThree3(self, n):
        while n % 3 == 0 and n != 0:
            n /= 3
        if n == 1: return True
        return False




# 1001209191712094
s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
# print(s.powerOfThree3(27))
# print(s.powerOfThree3(4))
# print(s.powerOfThree3(15))
# print(s.trailingZeroes(4))
# print (s.plusOne([1,2,3,4]))
# print(s.isPalindrome(1001209191712094209421))
# print (s.countAndSay(1211))
# print (s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print (s.twoSum([2, 7, 11, 15], 9))
# print (s.twoSUm([2, 7, 11, 15], 9))
# print (s.removeDuplicates([1,1,2]))
# print (s.removeDuplicates([0,0,0,0,0,0,0,0,0,0,1,1,2,3]))
# print (s.maxSubArrayGoogle([-2,1,-3,4,-1,2,1,-5,4]))
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
# print (s.intersect([1,2,2,1], [2]))//
# print(s.maxProfitOneTx([7,1,5,3,6,4]))
# print (s.isHappy(19))
# print(s.hammingWeight(8763234))
# print(s.hamming2(8763234))
