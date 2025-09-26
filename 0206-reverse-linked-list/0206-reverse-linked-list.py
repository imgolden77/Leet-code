# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        # 2. curr 포인터를 head로 초기화하여 리스트 순회를 시작합니다.
        curr = head
        
        # curr가 None이 될 때까지 (리스트의 끝에 도달할 때까지) 반복합니다.
        while curr:
            # 3. next_temp에 다음 노드를 임시로 저장합니다. 
            #    (연결을 끊기 전에 다음 노드의 주소를 잃어버리지 않기 위함)
            next_temp = curr.next
            
            # 4. 핵심: 현재 노드의 next 포인터를 이전 노드(prev)로 바꿉니다. (방향 역전)
            curr.next = prev
            
            # 5. prev와 curr 포인터를 다음 위치로 이동합니다.
            prev = curr
            curr = next_temp
            
        # 반복문이 끝나면, prev는 원래 리스트의 마지막 노드(새로운 head)를 가리킵니다.
        return prev
        