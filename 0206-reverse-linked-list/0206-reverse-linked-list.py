# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr is not None:
            if prev:
                post = curr.next
                curr.next = prev
                prev = curr
                curr = post
            else:
                post = curr.next
                prev = curr
                curr.next = None
                curr = post

        return prev