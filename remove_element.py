# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for element in range(len(nums)):
            if nums[element] != val :
                nums[i] = nums[element]
                i+=1
        return i
        
