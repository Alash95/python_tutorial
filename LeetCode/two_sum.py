"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if (num1 + num2 == target) and (i != j) and (2 <= len(nums) <= (10 ** 4)) and ((-10 ** 9) <= num1 
                <= (10 ** 9)) and ((-10 ** 9) <= target <= (10 ** 9)):
                    return  [i, j]


    def twoSum1(self, nums, target):
        number_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in number_map:
                return [i, number_map[diff]]
            
            number_map[num] = i

        return None
    
sol = Solution()
nums = [2,7,11,15]
target = 9

print(sol.twoSum(nums, target))
print(sol.twoSum1(nums, target))


            