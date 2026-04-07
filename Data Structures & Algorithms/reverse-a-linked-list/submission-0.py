# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            # 1. Temporarily store the next node
            nxt = curr.next
            
            # 2. Reverse the current node's pointer
            curr.next = prev
            
            # 3. Move pointers one position forward
            prev = curr
            curr = nxt
            
        # At the end, prev will be the new head
        return prev