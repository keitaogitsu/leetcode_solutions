#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        def number_replace(str_current: str, str_next: str) -> int:
            if str_current == "I":
                if str_next == "V":
                    return 4
                elif str_next == "X":
                    return 9
                else:
                    return 1
            elif str_current == "X":
                if str_next == "L":
                    return 40
                elif str_next == "C":
                    return 90
                else:
                    return 10
            elif str_current == "C":
                if str_next == "D":
                    return 400
                elif str_next == "M":
                    return 900
                else:
                    return 100
        
        parse = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        i = 0
        n = len(s)
        while i < n:
            if i < n-1 and parse[s[i]] < parse[s[i+1]]:
                sum += number_replace(s[i], s[i+1])
                i += 2
            else:
                sum += parse[s[i]]
                i += 1
        return sum 
# @lc code=end

