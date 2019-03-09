#Answer to DI String Match - https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        I = 0
        D = len(S)
        res = []
        for i in S:
            if i == 'I':
                res.append(I)
                I+=1
            else:
                res.append(D)
                D-=1
        if S[len(S)-1] == 'I':
            res.append(I)
        else:
            res.append(D)
        return res