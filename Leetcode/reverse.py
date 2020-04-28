class Solution:
    def reverseString(self, s):
        """Two Pointers Approach
            In this approach, two pointers are used to process two array elements at the same time. Usual implementation is to set one pointer in the beginning and one at the end and then to move them until they both meet.
            Sometimes one needs to generalize this approach in order to use three pointers, like for classical Sort Colors problem.
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
        return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])

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
            d[i] = d.get(i,0)+1
        for key, val in d.items():
            if val ==1:
                return key

    def single_number2(self, nums):
        res = 1
        for i in nums:
            res = res ^ i
            print ("res==", res)
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
                count+=1
        while count < n:
            nums[count] = 0
            count +=1
        return nums

    def move_zeros_to_beginning(self, nums):
        n = len(nums)
        read_pointer = n - 1
        write_pointer = n - 1
        while (read_pointer >=0):
                if nums[read_pointer] != 0:
                    nums[write_pointer] = nums[read_pointer]
                    write_pointer-=1
                read_pointer-=1

        while (write_pointer>=0):
            nums[write_pointer]= 0
            write_pointer-=1
        return nums



s = Solution()
# print(s.reverseString("Nikhil"))
# print(s.reverseRecursive("Nikhil"))
# print (s.single_number2([4,4,2, 2,1]))
# print (s.move_zeros_to_end([1,2,0,9,8,0,9,8,7,6,90,0,0,0,1,1,1,1,1]))
print (s.move_zeros_to_beginning([1, 10, 20, 0, 59, 63, 0, 88, 0]))
