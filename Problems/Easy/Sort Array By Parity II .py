# Answer to Sort Array By Parity II
# https://leetcode.com/problems/sort-array-by-parity-ii/


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j, B = 0, 1, [0] * len(A)
        for k in A:
            if k%2 == 0:
                B[i] = k
                i += 2
            else:
                B[j] = k
                j += 2
        return B


"""
# You can also solve it in the below method

class Solution1:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd, even = [], []
        for i in A:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        A = []
        for i in range(len(odd)):
            A.append(even[i])
            A.append(odd[i])
        return A
"""