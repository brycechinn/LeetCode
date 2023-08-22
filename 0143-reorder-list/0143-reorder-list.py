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
        
        # approach: split list in half, reverse right half, alternate
        # nodes
        
        # get midpoint
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        left = head
        
        # reverse right half
        prev = None
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp

        # reorder list
        right = prev
        while left and right:
            temp = left.next
            left.next = right
            left = temp
            
            temp = right.next
            right.next = left
            right = temp