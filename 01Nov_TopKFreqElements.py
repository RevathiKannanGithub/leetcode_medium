#
# https://leetcode.com/problems/top-k-frequent-elements/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_nums = Counter(nums)
        sort_counter_nums = sorted(counter_nums.keys(), key=lambda x: -counter_nums[x])
        print(sort_counter_nums[:k])
        return sort_counter_nums[:k]
