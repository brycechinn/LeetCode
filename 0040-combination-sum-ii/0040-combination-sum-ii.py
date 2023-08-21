class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # approach: backtracking DFS, prevent duplicate combinations
        # by sortings nums first and skipping duplicates before
        # right decision branch
        
        candidates.sort()
        res, combo = [], []
        
        def dfs(i, total):
            if total == target:
                res.append(combo.copy())
                return
            
            if i == len(candidates) or total > target:
                return
                
            num = candidates[i]
        
            # include num
            combo.append(num)
            dfs(i + 1, total + num)
            
            # skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            # don't include num
            combo.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res