"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # approach: DFS, hashmap of old node : new node
        
        if not node:
            return None
        
        hashmap = {}
        
        def dfs(node):
            if node in hashmap:
                return hashmap[node]

            copy = Node(node.val)
            hashmap[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
                
            return copy
        
        return dfs(node)