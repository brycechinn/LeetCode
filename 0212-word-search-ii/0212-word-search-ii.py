class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.refs = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        curr.refs += 1
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
                
            curr = curr.children[c]
            curr.refs += 1
        
        curr.end = True
        
    def removeWord(self, word):
        curr = self.root
        curr.refs -= 1
        
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # approach: trie + backtracking, keep track of node refs, 
        # prune tree when word found
        
        ROWS, COLS = len(board), len(board[0])
        path_set = set()
        path = ''
        res = set()
        
        trie = Trie()
        
        for w in words:
            trie.addWord(w)
        
        def dfs(r, c, curr):
            nonlocal path
            
            if (r not in range(ROWS) or
                c not in range(COLS) or
                board[r][c] not in curr.children or
                curr.children[board[r][c]].refs < 1 or
                (r, c) in path_set):
                
                return

            path += board[r][c]
            path_set.add((r, c))
            curr = curr.children[board[r][c]]
            
            if curr.end:
                curr.end = False
                res.add(path)
                trie.removeWord(path)
            
            dfs(r + 1, c, curr)
            dfs(r - 1, c, curr)
            dfs(r, c + 1, curr)
            dfs(r, c - 1, curr)
            
            # backtrack
            path = path[:-1]
            path_set.remove((r, c))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root)
        
        return list(res)
            
            
            
            
                
                
            
        
        
        