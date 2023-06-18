/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // approach 1: get length of list then remove length - nth node
        
        /*
        if (head.next == null) {
            return null;
        }
        
        int length = 0;
        ListNode curr = head;
        
        while (curr != null) {
            length++;
            curr = curr.next;
        }
        
        // 1-indexed
        int index = length - n + 1;
        ListNode prev = null;
        curr = head;
        int count = 0;
        
        while (curr != null) {
            count++;
            
            if (count == index) {
                
                if (prev == null) {
                    return curr.next;
                } else {
                    prev.next = curr.next;
                }
                
                break;
            }
            
            prev = curr;
            curr = curr.next;
        }
        
        return head;
        */
        
        // approach 2: two pointers, one at dummy node and one at head + n
        
        if (head.next == null) {
            return null;
        }
        
        ListNode dummy = new ListNode();
        dummy.next = head;
        
        ListNode left = dummy;
        ListNode right = head;
        
        for (int i = 0; i < n; i++) {
            right = right.next;
        }
        
        while (right != null) {
            left = left.next;
            right = right.next;
        }
        
        left.next = left.next.next;
        
        return dummy.next;
    }
}