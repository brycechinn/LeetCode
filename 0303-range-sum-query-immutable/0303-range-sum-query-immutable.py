'''
# approach 1: straightforward solution
# time: O(n)
# space: O(n)

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sub = self.nums[left:right + 1]
        return sum(sub)

# approach 2: cache query results
# time: O(n)
# space: O(n)

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
'''

# approach 3: prefix sum array
# time: O(1)
# space: O(n)

class NumArray:

    def __init__(self, nums: List[int]):
        self.sums, total = [], 0
        
        for i, num in enumerate(nums):
            total += num
            self.sums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        left_sum, right_sum = self.sums[left - 1] if left > 0 else 0, self.sums[right]
        return right_sum - left_sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)