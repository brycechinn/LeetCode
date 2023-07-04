class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # approach: backtracking, include num and don't increment i or don't
        # include num and increment i
        
        res, combo = [], []
        
        def dfs(i, total):
            if total == target:
                res.append(combo.copy())
                return
            
            if total > target or i == len(candidates):
                return
            
            # include num, don't increment i
            combo.append(candidates[i])
            dfs(i, total + candidates[i])
            
            # don't include num, increment i
            combo.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res
        
        