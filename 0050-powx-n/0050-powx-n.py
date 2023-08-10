class Solution:
    def myPow(self, x: float, n: int) -> float:
        # approach: divide and conquer via recursion, return 1 / res if n < 0
        
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = helper(x, n // 2)
            res *= res
            return x * res if n % 2 else res
        
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res