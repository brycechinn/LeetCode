class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # combination sum
        
        candidates.sort()
        
        combo, res = [], []
        
        def dfs(i, total):
            if total == target:
                res.append(combo.copy())
                print(combo)
                return
            
            if total > target or i == len(candidates):
                return
            
            # include num
            combo.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            
            # don't include num
            combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, total)
            
        dfs(0, 0)
        return res