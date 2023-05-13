class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # approach: dict to store num frequency, then sort dict
        
        if len(nums) == 1:
            return nums
        
        d = {}
        res = []
        
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
                  
        sd = sorted(d.items(), key=lambda x:x[1], reverse=True)
        
        for i in range(k):
            item = sd[i]
            res.append(item[0])

        return res