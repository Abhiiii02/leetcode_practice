#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. 
#You may assume that the majority element always exists in the array.

 


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        req = len(nums) // 2
        nums.sort()
        i = 0 
        while i < len(nums):
            if nums[i] == nums[i + req]:
                break
            i+=1
        return nums[i]