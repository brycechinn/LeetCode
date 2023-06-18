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
        // approach: two pointers, one at dummy node and one at head + n
        
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