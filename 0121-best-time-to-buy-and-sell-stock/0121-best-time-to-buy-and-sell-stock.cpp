class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int result = 0;
        int minimum = prices[0];
        
        for (int price : prices) {
            minimum = min(minimum, price);
            int profit = price - minimum;
            result = max(result, profit);
        }
        
        return result;
    }
};