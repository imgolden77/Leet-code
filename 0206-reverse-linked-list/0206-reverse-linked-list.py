# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        temp_next=None 

        while curr is not None:
            prev =curr
            curr = curr.next
            prev.next = temp_next
            temp_next = prev

        return prev
            
            
    
        while num:
            # print("num:", num)
            res.val = num.pop()
            if len(num)==0:
                res.next = None
                # print("debug1:", head_res)
            else:
                res.next = ListNode()
                res = res.next
                # print("debug2:", head_res)

            
        return(head_res)
            