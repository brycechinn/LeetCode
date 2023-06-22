class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # approach: hasmap of num : frequency then list of frequency : list of nums
        
        hashmap = collections.defaultdict(int)
        counts = [[] for _ in range(len(nums) + 1)] 
        result = []
        
        for num in nums:
            hashmap[num] += 1

        for num in hashmap:
            freq = hashmap[num]
            counts[freq].append(num)

        for i in reversed(range(len(counts))):
            for num in counts[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        