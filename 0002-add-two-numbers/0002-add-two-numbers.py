# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        # approach: elementary addition, keep track of carry
    
        carry = 0
        head = ListNode()
        curr = head

        while l1 or l2:
            top = l1.val if l1 else 0
            bot = l2.val if l2 else 0

            result = carry + top + bot
            carry = 0

            if result > 9:
                result = result - 10
                carry = 1

            curr.next = ListNode(result)
            curr = curr.next
            
            if l1:
                l1 = l1.next
                
            if l2:
                l2 = l2.next

        if carry:
            curr.next = ListNode(carry)

        return head.next
        
        