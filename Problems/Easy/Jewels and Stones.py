#Answer to Jewels and Stones - https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for i in J:
            total+=S.count(i)
        return total