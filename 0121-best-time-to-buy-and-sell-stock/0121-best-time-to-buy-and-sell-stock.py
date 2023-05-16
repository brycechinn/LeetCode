class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # approach 1: store low and maxProfit

        '''
        low, maxProfit = prices[0], 0
        
        for price in prices:
            low = min(low, price)
            maxProfit = max(maxProfit, price - low)
        
        return maxProfit
        '''
    
        # approach 2: two pointers
        
        l, r = 0, 1
        maxProfit = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            
            r += 1
        
        return maxProfit
                
                
    
        
        