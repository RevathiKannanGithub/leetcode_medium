#
# https://leetcode.com/problems/longest-consecutive-sequence/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
# 
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. 
# You must write an algorithm that runs in O(n) time.
#
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        nums.sort()
        
        curr_count = 1
        max_count = 0
        curr = nums[0]

        for i in nums:
            if curr + 1 == i:
                curr_count += 1
                max_count = max(max_count, curr_count)
            elif curr == i:
                pass
            else:
                curr_count = 1
            curr = i
        max_count = max(max_count, curr_count)

        return max_count
