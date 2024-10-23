class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        # approach 1: O(mn) solution where m = len(nums1), n = len(nums2)
        
        res = []
        
        for num1 in nums1:
            num1_index = nums2.index(num1)
            found = False
            
            for i in range(num1_index + 1, len(nums2)):
                num2 = nums2[i]
                
                if num2 > num1:
                    res.append(num2)
                    found = True
                    break
            
            if not found:
                res.append(-1)
        
        return res
        '''
    
        # approach 2: O(m + n) solution where m = len(nums1), n = len(nums2)
        
        stack, d, res = [], {}, [-1] * len(nums1)
        
        for i, num1 in enumerate(nums1):
            d[num1] = i
        
        for num2 in nums2:
            if not stack:
                stack.append(num2)
                continue
                
            while stack and num2 > stack[-1]:
                val = stack.pop()
                
                if val in d:
                    index = d[val]
                    res[index] = num2
                
            stack.append(num2)
        
        return res