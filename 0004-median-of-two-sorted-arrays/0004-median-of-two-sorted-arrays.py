class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # approach: binary search on the smaller of nums1 and nums2
        # to find a valid left portion
        
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(A) > len(B):
            A, B = B, A # python swap
        
        l, r = 0, len(A) - 1
        while True: # guaranteed median
            i = (l + r) // 2
            j = half - i - 2
            
            leftA = A[i] if i >= 0 else float('-inf')
            rightA = A[i + 1] if (i + 1) < len(A) else float('inf')
            leftB = B[j] if j >= 0 else float('-inf')
            rightB = B[j + 1] if (j + 1) < len(B) else float('inf')
            
            if leftA > rightB:
                # too many elements from A
                r = i - 1
            elif leftB > rightA:
                # too many elements from B
                l = i + 1
            else:
                if total % 2:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
        
    