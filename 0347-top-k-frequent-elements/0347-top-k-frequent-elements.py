class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # approach 1: dict to store num frequency, then sort dict
        
        '''
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
        '''
        
        # approach 2: dict to store num frequency, array of frequency -> nums
        
        if len(nums) == 1:
            return nums
        
        d = {}
        res = []
        
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        arr = [[] for i in range(len(nums) + 1)]
        
        for num in d:
            freq = d[num]
            arr[freq].append(num)
        
        for i in reversed(range(len(arr))):
            for num in arr[i]:
                res.append(num)
                
                if len(res) == k:
                    return res
        
        
        
        
        
        
        
        