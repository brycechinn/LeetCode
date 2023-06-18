/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        // approach: two passes, first to make hashmap of old node : copied node,
        // second to connect ptrs
        
        Map<Node, Node> hashmap = new HashMap<>();
        hashmap.put(null, null); // edge case
        
        Node curr = head;
        
        while (curr != null) {
            Node copy = new Node(curr.val);
            hashmap.put(curr, copy);
            curr = curr.next;
        }
        
        curr = head;
        
        while (curr != null) {
            Node copy = hashmap.get(curr);
            copy.next = hashmap.get(curr.next);
            copy.random = hashmap.get(curr.random);
            curr = curr.next;
        }
        
        return hashmap.get(head);
    }
}