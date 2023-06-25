class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        lowest = prices[0]
        
        for price in prices:
            lowest = min(lowest, price)
            profit = price - lowest
            result = max(result, profit)
        
        return result