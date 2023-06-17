class MinStack {
    // approach: maintain adjacent stack of mins at each node
    
    private Stack<Integer> stack;
    private Stack<Integer> mins;
    
    public MinStack() {
        this.stack = new Stack<>();
        this.mins = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        
        if (mins.isEmpty()) {
            mins.push(val);
        } else {
            if (val < mins.peek()) {
                mins.push(val);
            } else {
                mins.push(mins.peek());
            }
        }
    }
    
    public void pop() {
        stack.pop();
        mins.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return mins.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */