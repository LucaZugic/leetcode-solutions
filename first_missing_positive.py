# Given an unsorted integer array nums, find the smallest missing positive integer.
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # if nums is emtpy, first pos int is 1
        if not nums:
            return 1
        maxnum = max(nums) # for speed we assign max of nums to var maxnum
        # if maxnum is neg in or 0, first pos int is 1
        if maxnum < 1:
            return 1     
        # else, for all in from 1 to maxnum + 2, return the first missing int
        else:
            for i in range(1, (maxnum+2)):
                if i not in nums:
                    return i
                    
