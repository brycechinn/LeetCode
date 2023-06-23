class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # approach: two pointers
        
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            left = numbers[l]
            right = numbers[r]
            
            total = left + right
            
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [l + 1, r + 1]