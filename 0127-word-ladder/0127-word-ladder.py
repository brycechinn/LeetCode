class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # approach: adjacency list of pattern : list of words, then BFS to find 
        # shortest path
        
        if endWord not in wordList:
            return 0

        visited = set()
        adj = collections.defaultdict(list)
        res = 1
        
        wordList.append(beginWord)
       
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i + 1:]
                adj[pattern].append(w)

        q = collections.deque()
        q.append(beginWord)

        while q:
            size = len(q)
            for i in range(size):
                w = q.popleft()

                if w == endWord:
                    return res

                for i in range(len(w)):
                    pattern = w[:i] + '*' + w[i + 1:]

                    for n in adj[pattern]:
                        if n in visited:
                            continue

                        visited.add(n)
                        q.append(n)

            res += 1

        return 0