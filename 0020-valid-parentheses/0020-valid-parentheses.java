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
            
            if (stack.empty()) {
                if (closing.containsKey(p)) {
                    stack.push(p);
                } else {
                    return false;
                }
            } else {
                if (p == closing.get(stack.peek())) {
                    stack.pop();
                } else if (closing.containsKey(p)){
                    stack.push(p);
                } else {
                    return false;
                }
            }
        }
        
        return stack.empty();
    }
}