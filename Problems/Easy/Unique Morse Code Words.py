#Answer to Unique Morse Code Words - https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result = set()
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in words:
            temp = ''
            for j in i:
                temp += alphabet[ord(j)-97]
            result.add(temp)
        return len(result)