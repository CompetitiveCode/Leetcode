#Answer to Squares of a Sorted Array - https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(i ** 2 for i in A)