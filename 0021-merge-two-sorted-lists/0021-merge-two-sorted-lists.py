# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # approach: dummy head and prev ptr
        
        dummy = ListNode()
        prev = dummy
        
        while list1 and list2:
            if list2.val < list1.val:
                prev.next = list2
                list2 = list2.next
            else:
                prev.next = list1
                list1 = list1.next
            
            prev = prev.next
        
        if list1:
            prev.next = list1
        elif list2:
            prev.next = list2
        
        return dummy.next
                