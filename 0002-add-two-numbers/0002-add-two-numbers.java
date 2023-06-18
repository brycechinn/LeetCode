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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // approach: elementary addition
        
        int carry = 0;
        int top = 0;
        int bot = 0;
        
        ListNode dummy = new ListNode();
        ListNode curr = dummy;
        
        while (l1 != null || l2 != null) {
            
            if (l1 == null) {
                top = 0;
            } else {
                top = l1.val;
            }
            
            if (l2 == null) {
                bot = 0;
            } else {
                bot = l2.val;
            }
            
            int sum = carry + top + bot;
            carry = 0;
            
            if (sum > 9) {
                carry = sum / 10;
                sum = sum % 10;
            }
            
            curr.next = new ListNode(sum);
            curr = curr.next;

            if (l1 != null) {
                l1 = l1.next;
            }
            
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        
        if (carry > 0) {
            curr.next = new ListNode(carry);
        }
        
        return dummy.next;
    }
}