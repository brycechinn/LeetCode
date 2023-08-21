class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # approach: backtracking DFS; include number and don't increment i
        # or don't include number and increment i
        
        res, path = [], []
        
        def dfs(i, total):
            if i == len(candidates) or total > target:
                return
            
            if total == target:
                res.append(path.copy())
                return
            
            num = candidates[i]
            
            path.append(num)
            dfs(i, total + num)
            
            # backtrack
            path.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res