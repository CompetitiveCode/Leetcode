#Answer to Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xo = format(x,'b')
        yo = format(y,'b')
        if len(xo) < len(yo):
            xo = xo.zfill(len(yo))
        else:
            yo = yo.zfill(len(xo))
        return sum(ch1 != ch2 for ch1,ch2 in zip(xo,yo))