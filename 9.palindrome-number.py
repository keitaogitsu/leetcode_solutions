#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        len_x = len(str_num)
        for i in range(len_x):
            if str_num[i] != str_num[len_x - i - 1]:
                return False
        return True
            
# @lc code=end

