class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perm, res = [], []
        hashset = set()
        
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in nums:
                if n not in hashset:
                    hashset.add(n)
                    perm.append(n)
                    
                    dfs()
                    
                    hashset.remove(n)
                    perm.pop()    
                    
        dfs()
        return res