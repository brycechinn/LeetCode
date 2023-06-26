# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # approach: two pointers with offset, dummy node
        
        dummy = ListNode
        dummy.next = head
        
        left = dummy
        right = head
        offset = 0
        
        while offset < n:
            right = right.next
            offset += 1
        
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        return dummy.next