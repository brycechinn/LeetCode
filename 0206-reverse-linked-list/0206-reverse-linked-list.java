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
    public ListNode reverseList(ListNode head) {
        ListNode curr = new ListNode();
        ListNode prev = new ListNode();
        curr = head;
        prev = null;
        
        while (curr != null) {
            ListNode tmp = new ListNode();
            tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }
        
        return prev;
    }
}