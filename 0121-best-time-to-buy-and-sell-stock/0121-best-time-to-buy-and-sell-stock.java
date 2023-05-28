class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int result = 0;
        
        for (int price : prices) {
            min = Math.min(min, price);
            int profit = price - min;
            result = Math.max(result, profit);
        }
        
        return result;
    }
}