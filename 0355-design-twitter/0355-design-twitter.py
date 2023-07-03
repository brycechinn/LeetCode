class Twitter:

    def __init__(self):
        self.time = 0
        
        # hashmap of followerId : hashset of followeeId
        self.followers = collections.defaultdict(set)
        
        # hashmap of userId : list of (time, tweetId)
        self.posts = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap, feed = [], []
        
        for p in self.posts[userId]:
            heap.append(p)
        
        for f in self.followers[userId]:
            for p in self.posts[f]:
                heap.append(p)
                
        heapq.heapify(heap)
        
        count = 0
        while heap and count < 10:
            feed.append(heapq.heappop(heap)[1])
            count += 1
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            return
        
        self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)