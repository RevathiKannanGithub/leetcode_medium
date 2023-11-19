#
# https://leetcode.com/problems/product-of-array-except-self/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
# #
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
#  
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
import functools

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [i for i in nums if i != 0]
        if not temp:
            product = 1
        else:
            product = functools.reduce(lambda x, y: x * y, temp)

        count_zeros = 0
        for i in nums:
            if i == 0:
                count_zeros += 1

        res = []
        if count_zeros >=2:
            res = [0]*len(nums)
        elif count_zeros == 1:
            res = [0]*len(nums)
            idx = nums.index(0)
            res[idx] = product
        else:
            for i in range(len(nums)):
                res.append(product//nums[i])
        return res
