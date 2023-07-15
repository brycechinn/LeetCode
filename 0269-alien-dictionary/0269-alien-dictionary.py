class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # approach: topological sort, i.e. DFS but build result in reverse order
        # via postorder traversal
        
        # step 1: build adjacency list
        adj = { c : set() for w in words for c in w }
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            shortest = min(len(w1), len(w2))
            
            # invalid if words have same prefix but second word is longer
            
            if len(w1) > len(w2) and w1[:shortest] == w2[:shortest]:
                return ''
            
            for j in range(shortest):
                c1, c2 = w1[j], w2[j]
                
                if c1 != c2:
                    adj[c1].add(c2)
                    break
        
        # step 2: topological sort via DFS
        visited, cycle = set(), set()
        has_cycle = False
        res = []
        
        def dfs(c):
            nonlocal has_cycle
            
            if c in cycle:
                has_cycle = True
                return
            
            if c in visited:
                return
            
            cycle.add(c)
            
            for nei in adj[c]:
                dfs(nei)
            
            cycle.remove(c)
            visited.add(c)
            res.append(c)
        
        for c in adj:
            dfs(c)
        
        res.reverse()
        return ''.join(res) if not has_cycle else ''