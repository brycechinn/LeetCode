class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int[] result = new int[temperatures.length];
        
        for (int i = 0; i < temperatures.length; i++) {
            int temp = temperatures[i];
            
            while (!stack.isEmpty() && temp > temperatures[stack.peek()]) {
                int top = stack.pop();
                result[top] = i - top;
            }
            
            stack.push(i);
        }
        
        return result;
    }
}