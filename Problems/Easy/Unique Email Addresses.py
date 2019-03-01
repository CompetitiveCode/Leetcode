#Answer to Unique Email Addresses - https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for i in emails:
            k = i.split('@')
            l = k[0].replace('.','')
            temp = ''
            flag = 0
            for j in l:
                if j!='+' and flag == 0:
                    temp += j
                else:
                    flag = 1
            temp+='@'+k[1]
            result.add(temp)
        return len(result)