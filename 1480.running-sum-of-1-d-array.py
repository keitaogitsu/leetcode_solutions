#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        answer[0] = nums[0]
        for i in range(1, len(nums)):
            answer[i] = nums[i] + answer[i-1]
        return answer
# @lc code=end

