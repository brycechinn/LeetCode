class Twitter:
    # approach: followers: hashmap of followerId : hashset of followeeId,
    # posts: hashmap of userId : list of (time, tweetId)
    
    def __init__(self):
        self.time = 0
        self.followers = defaultdict(set)
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap, feed = [], []
        
        # user follows themself
        self.followers[userId].add(userId)
        
        for followeeId in self.followers[userId]:
            if followeeId in self.posts:
                index = len(self.posts[followeeId]) - 1
                time, tweetId = self.posts[followeeId][index]
                heapq.heappush(heap, (time, tweetId, followeeId, index - 1))
                
        heapq.heapify(heap)

        while heap and len(feed) < 10:
            time, tweetId, followeeId, index = heapq.heappop(heap)
            feed.append(tweetId)
            
            if index >= 0:
                time, tweetId = self.posts[followeeId][index]
                heapq.heappush(heap, (time, tweetId, followeeId, index - 1))
            
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