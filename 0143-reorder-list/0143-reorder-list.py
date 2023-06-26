# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # approach:
        # 1. find middle of list with slow and fast ptr
        # 2. reverse right half of list
        # 3. alternate adding nodes from left and right half, working inward
        
        # 1. find middle of list with slow and fast ptr
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. reverse right half of list
        prev = None
        curr = slow.next
        slow.next = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left = head
        right = prev
        
        # 3. alternate adding nodes from left and right half, working inward
        while left and right:
            temp = left.next
            left.next = right
            left = temp
            
            temp = right.next
            right.next = left
            right = temp
        
        return head