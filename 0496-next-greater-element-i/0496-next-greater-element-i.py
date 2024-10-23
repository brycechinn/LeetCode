class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
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