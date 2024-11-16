class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # approach 1: brute force
        # time: O(n^2), space: O(1)
        '''
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j and nums[i] == nums[j]:
                    res += 1
        
        return res
        '''
    
        # approach 2: hashmap to count num occurrences, triangular number formula
        # time: O(n), space: O(n)
        counts, res = Counter(nums), 0
        
        for count in counts.values():
            res += self.triangularNumberFormula(count - 1)
        
        return res
    
    def triangularNumberFormula(self, n: int) -> int:
        # will always be a whole number
        return (n * (n + 1)) // 2