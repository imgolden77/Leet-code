# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head)
        curr = head
        num=[]

        if curr is None:
            head_res = None
        else:
            res = ListNode()
            head_res = res

        while curr is not None:
            num.append(curr.val)
            curr = curr.next
    
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
            