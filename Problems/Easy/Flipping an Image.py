#Answer to Flipping an Image - https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            l = len(A[i])
            k = [0 for j in range(l)]
            for j in range(l):
                if A[i][j] == 1:
                    k[l-j-1] = 0
                else:
                    k[l-j-1] = 1
            A[i] = k
        return A