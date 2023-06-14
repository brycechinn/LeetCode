class Solution {
    public int maxProfit(int[] prices) {
        // approach: keep track of current min
        
        int min = prices[0];
        int result = 0;
        
        for (int price : prices) {
            if (price < min) {
                min = price;
            }
            
            result = Math.max(result, price - min);
        }
        
        return result;
    }
}