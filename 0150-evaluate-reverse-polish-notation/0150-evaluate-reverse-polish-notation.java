class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        Set<String> ops = new HashSet<>();
        
        ops.add("+");
        ops.add("-");
        ops.add("*");
        ops.add("/");

        for (String str : tokens) {
            if (ops.contains(str)) {
                // handle operator
                int right = stack.pop();
                int left = stack.pop();
                
                if (str.equals("+")) {
                    stack.push(left + right);
                } else if (str.equals("-")) {
                    stack.push(left - right);
                } else if (str.equals("*")) {
                    stack.push(left * right);
                } else {
                    stack.push(left / right);
                }
            } else {
                // handle num
                int num = Integer.valueOf(str);
                stack.push(num);
            }
        }
        
        // last element is result
        return stack.pop();
    }
}