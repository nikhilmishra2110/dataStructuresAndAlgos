# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = curr = ListNode(0)
#         while l1 and l2:
#              if l1.val < l2.val:
#                  curr.next = l1
#                  l1 = l1.next
#              else:
#                  curr.next=l2
#                  l2= l2.next
#              curr = curr.next
#         curr.next = l1 or l2
#         print (curr.next.val)
#         return dummy.next
#



def square(num):
    return num**2

print (square(23123))
print (square(123))
print (square(123))
print (square(2323))
print (square(2323))
print (square(23))
# print (squar3123))



gma = [1,2,3,4,5,6,7,8,9,6,5,4,4,2,2]


print((list(map(square, gma))))