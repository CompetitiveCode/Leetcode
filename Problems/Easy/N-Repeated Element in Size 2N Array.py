#Answer to N-Repeated Element in Size 2N Array - https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        length = len(A)//2
        for i in A:
            if A.count(i) == length:
                return i