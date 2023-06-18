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
        // approach: get length of list then remove length - nth node
        
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
    }
}