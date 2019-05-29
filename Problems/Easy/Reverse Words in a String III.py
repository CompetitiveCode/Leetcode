# Answer to Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for i in s.split():
            res.append(''.join(reversed(i)))
        return ' '.join(res)
