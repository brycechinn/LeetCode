class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # combination sum, but sort nums first and skip duplicates before 
        # entering right decision branch
        
        candidates.sort()
        combo, res = [], []
        
        def dfs(i, total):
            if total == target:
                res.append(combo.copy())
                return
            
            if total > target or i == len(candidates):
                return

            combo.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)
            
        dfs(0, 0)
        return res