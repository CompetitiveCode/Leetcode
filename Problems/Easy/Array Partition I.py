# Answer to Array Partition I
# https://leetcode.com/problems/array-partition-i/


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res
