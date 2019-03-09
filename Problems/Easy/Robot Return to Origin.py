#Answer to Robot Return to Origin - https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {'R':0,'L':0,'U':0,'D':0}
        for i in moves:
            d[i] += 1
        if d['R'] == d['L'] and d['U'] == d['D']:
            return True
        return False