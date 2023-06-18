public class Node {
    public int key;
    public int val;
    public Node prev;
    public Node next;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
    
}

class LRUCache {
    private int capacity;
    private Map<Integer, Node> hashmap = new HashMap<>();
    private Node left;
    private Node right;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        left = new Node(0, 0);
        right = new Node(0, 0);
        
        left.next = right;
        left.prev = null;
        
        right.next = null;
        right.prev = left;
    }
    
    private void remove(Node node) {
        // remove node from current pos in list
        Node prev = node.prev;
        Node next = node.next;
        
        prev.next = next;
        next.prev = prev;
    }
    
    private void append(Node node) {
        // add node to right of list
        Node temp = right.prev;
        right.prev = node;
        node.next = right;
        node.prev = temp;
        temp.next = node;
    }
    
    public int get(int key) {
        System.out.println("getting " + key);
        
        if (!hashmap.containsKey(key)) {
            return -1;
        }
        
        Node node = hashmap.get(key);
        
        // remove node from current pos in list
        remove(node);
        
        // add node to right of list
        append(node);
        
        return node.val;
    }
    
    public void put(int key, int value) {
        if (hashmap.containsKey(key)) {
            // key already exists, so remove old one
            remove(hashmap.get(key));
            hashmap.remove(key, hashmap.get(key));
            capacity++;
        }
        
        // add key to hashmap and add node to list
        Node node = new Node(key, value);
        hashmap.put(key, node);
        append(node);
        capacity--;
        
        System.out.println("putting " + key + ", capacity now " + capacity);
        // remove LRU if capacity exceeded
        if (capacity < 0) {
            Node lru = left.next;
            remove(lru);
            hashmap.remove(lru.key, lru);
            capacity++;
            System.out.println("removed " + lru.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */