#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack1 = []
        stack2 = []
        for num in nums:
            if num in stack1:
                stack2.append(num)
            else:
                stack1.append(num)
        answer = list(set(stack1) - set(stack2))
        return answer[0]
        
