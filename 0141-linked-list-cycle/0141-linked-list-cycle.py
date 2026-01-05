# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         curr = head 
#         while curr.next != None:
#             fast = curr.next.next
#             slow = curr
#             if slow
        
#         return false

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        values = set()

        while curr:
            if curr in values:
                return True
           
            values.add(curr)
            curr = curr.next

        return False