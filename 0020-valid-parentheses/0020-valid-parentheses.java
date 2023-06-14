class Solution {
    public boolean isValid(String s) {
        // approach: stack, think of cases for stack empty vs. not empty
        
        Map<Character, Character> closing = new HashMap<>();
        
        closing.put('(', ')');
        closing.put('{', '}');
        closing.put('[', ']');
        
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            char p = s.charAt(i);
            
            if (closing.containsKey(p)) {
                stack.push(p);
                continue;
            }
            
            if (stack.empty()) {
                return false;
            }
            
            if (p == closing.get(stack.peek())){
                stack.pop();
            } else {
                return false;
            }
        }
        
        return stack.empty();
    }
}