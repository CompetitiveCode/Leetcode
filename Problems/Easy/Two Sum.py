#Answer to Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        k = len(nums) #To get the length of the list
        for i in range(k): #Parsing through each value of the list
            if target-nums[i] in nums: #We should only check the rest if there is a number which adds up with nums[i] to give target
                for j in range(k): #If there is a number like that, then we should get it's index number
                    if nums[j] == target-nums[i] and j != i: #We should also make sure that we do not take the index number of i
                        return i,j #Once we find a pair like that, just return that value