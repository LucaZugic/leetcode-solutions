# Median of two sorted arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        x = len(nums)
        if x % 2 ==0:
            median = (nums[int(x/2-1)] + nums[int(x/2)])/2
        else:
            median = nums[int(x/2)]
        return median
        
