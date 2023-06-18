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
    public void reorderList(ListNode head) {
        
        // approach: split list in half, reverse links in right half, then use
        // two pointers to reorder nodes
        
        // split list in half using slow and fast ptr
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // first node in right half
        ListNode right = slow.next;
        
        // make end of left half null
        slow.next = null;
        
        System.out.println(slow.val);
        
        // reverse right half
        ListNode prev = null;
        
        while (right != null) {
            ListNode temp = right.next;
            right.next = prev;
            prev = right;
            right = temp;
        }
        
        ListNode left = head;
        right = prev;
        
        while (left != null && right != null) {
            ListNode temp = left.next;
            left.next = right;
            left = temp;
            
            temp = right.next;
            right.next = left;
            right = temp;
        }
        
        ListNode curr = head;
        while (curr != null) {
            System.out.print(curr.val + " ");
            curr = curr.next;
        }
    }
}