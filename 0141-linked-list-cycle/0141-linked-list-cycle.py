# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        rabbit = head

        while turtle is not None and rabbit is not None and rabbit.next is not None:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if turtle == rabbit:
                return True
        
        return False