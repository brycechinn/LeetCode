class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> hashmap = new HashMap<>();
        
        hashmap.put('(', ')');
        hashmap.put('{', '}');
        hashmap.put('[', ']');
        
        Stack<Character> stack = new Stack<>();
        
        for (char c : s.toCharArray()) {
            if (hashmap.containsKey(c)) {
                stack.push(c);
            } else {
                if (!stack.empty() && c == hashmap.get(stack.peek())) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        
        return stack.empty();
    }
}