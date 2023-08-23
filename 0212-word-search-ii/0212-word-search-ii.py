class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.refs = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        curr.refs += 1
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
            curr.refs += 1
        
        curr.end = True
    
    def remove(self, word):
        curr = self.root
        curr.refs -= 1
        
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # approach: trie + backtracking, keep track of node refs, prune trie
        # when word found
        
        m, n = len(board), len(board[0])
        t = Trie()
        
        for w in words:
            t.insert(w)
        
        res, visited, path = set(), set(), []
        
        def dfs(r, c, node):
            if (r not in range(m) or 
                c not in range(n) or 
                (r, c) in visited or 
                board[r][c] not in node.children or 
                node.children[board[r][c]].refs < 1):
                return
            
            node = node.children[board[r][c]]
            path.append(board[r][c])
            
            w = ''.join(path)
            if node.end:
                res.add(w)
                node.end = False
                t.remove(w)
            
            visited.add((r, c))
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            
            for dr, dc in directions:
                dfs(r + dr, c + dc, node)
            
            path.pop()
            visited.remove((r, c))
        
        for r in range(m):
            for c in range(n):
                dfs(r, c, t.root)
        
        return list(res)