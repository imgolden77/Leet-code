# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        stack = []

        while curr is not None:
            if curr not in stack:
                stack.append(curr)
            else:
                return True
            curr=curr.next
        
        return False