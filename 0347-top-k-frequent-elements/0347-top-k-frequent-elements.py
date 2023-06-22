class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # approach: hasmap of num : frequency then list of frequency : list of nums
        
        hashmap = collections.defaultdict(int)
        result = []
        
        for num in nums:
            hashmap[num] += 1

        counts = [[] for _ in range(len(nums))] 

        for num in hashmap:
            freq = hashmap[num]
            counts[freq - 1].append(num)

        added = 0;
        for i in reversed(range(len(counts))):
            if counts[i]:
                for j in reversed(range(len(counts[i]))):
                    result.append(counts[i][j])
                    added += 1
                    if added == k:
                        return result
        
        