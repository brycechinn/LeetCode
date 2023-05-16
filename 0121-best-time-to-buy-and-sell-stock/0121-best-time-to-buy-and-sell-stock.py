class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # approach: store low and maxProfit
        
        low, maxProfit = prices[0], 0
        
        for price in prices:
            low = min(low, price)
            maxProfit = max(maxProfit, price - low)
        
        return maxProfit
        
        