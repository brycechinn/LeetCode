class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # adj = collections.defaultdict(set)
        visited = set()
        dists = {}
        
        wordList.append(beginWord)
        
        '''
        for w1 in wordList:
            for w2 in wordList:
                if w1 != w2 and self.areAdjacent(w1, w2):
                    adj[w1].add(w2)
                    adj[w2].add(w1)
        '''
        
        adj = collections.defaultdict(list)
        
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i + 1:]
                adj[pattern].append(w)
        
        for w in wordList:
            dists[w] = float('inf')
        
        dists[beginWord] = 0

        def bfs():
            q = collections.deque()
            q.append(beginWord)
            
            while q:
                w = q.popleft()
                
                for i in range(len(w)):
                    pattern = w[:i] + '*' + w[i + 1:]
                    
                    for n in adj[pattern]:
                        if n in visited:
                            continue
                    
                        visited.add(n)
                        dists[n] = min(dists[n], dists[w] + 1)
                        q.append(n)
                
                for n in adj[w]:
                    if n in visited:
                        continue
                    
                    visited.add(n)
                    dists[n] = min(dists[n], dists[w] + 1)
                    q.append(n)

        bfs()
        res = dists[endWord]

        return res + 1 if res != float('inf') else 0
            
        
    def areAdjacent(self, w1, w2):
        differences = 0
        
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                differences += 1
        
        return differences == 1