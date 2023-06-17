class Solution {
    List<String> result = new ArrayList<>();
    Stack<String> stack = new Stack<>();
    
    public List<String> generateParenthesis(int n) {
        // approach: backtracking using stack.pop()
        
        stack.push("(");
        backtrack(n, 1, 0);
        
        return result;
    }
    
    private void backtrack(int n, int numOpen, int numClosed) {
        if (numOpen == n && numClosed == n) {
            StringBuilder stringBuilder = new StringBuilder();
            stack.stream().forEach(p -> stringBuilder.append(p));
            
            result.add(stringBuilder.toString());
        }
        
        if (numOpen < n) {
            stack.push("(");
            backtrack(n, numOpen + 1, numClosed);
            stack.pop();
        }
        
        if (numClosed < numOpen) {
            stack.push(")");
            backtrack(n, numOpen, numClosed + 1);
            stack.pop();
        }
    }
}