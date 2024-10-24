# approach 1: straightforward solution
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sub = self.nums[left:right + 1]
        return sum(sub)
'''

# approach 2: cache query results

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cache = {}

    def sumRange(self, left: int, right: int) -> int:
        if (left, right) in self.cache:
            return self.cache[(left, right)]
        
        sub = self.nums[left:right + 1]
        res = sum(sub)
        self.cache[(left, right)] = res
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)