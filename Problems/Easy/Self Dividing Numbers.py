#Answer to Self Dividing Numbers - https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        final = []
        for i in range(left, right+1):
            temp = 0
            for j in str(i):
                if j == '0':
                    temp = 1
                elif i % int(j) != 0:
                    temp = 1
            if temp == 0:
                final.append(i)
        return final