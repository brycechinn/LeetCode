class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = nums.copy()

        for n in nums:
            res.append(n)

        return res