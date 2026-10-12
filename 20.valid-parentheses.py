#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        bracket_stack = []
        for c in s:
            if c in pair_dict.values():
                bracket_stack.append(c)
            else:
                if len(bracket_stack) == 0 or bracket_stack[-1] != pair_dict[c]:
                    return False
                bracket_stack.pop()
        return len(bracket_stack) == 0
# @lc code=end

# --- 最初に書いたコード ---
# class Solution:
#     def isValid(self, s: str) -> bool:
#         # 同じ種類のbracketがlで始まりrで終わっていれば、True
#         # あるbracketが始まって終わるまでの間に、別のbracketが始まっていてかつ終わっていなければFalseとする。
#         brackets_left = "([{"
#         brackets_right = "}])"
#         round_b_flag = True
#         square_b_flag = True
#         curly_b_flag = True
#         flags = [round_b_flag, square_b_flag, curly_b_flag]
        
#         for c in s:
#             for bracket_left in brackets_left:
#                 if c == bracket_left:
#                     flags[brackets_left.find(c)] = False
#             for bracket_right in brackets_right:
#                 if c == bracket_right and flags[brackets_left.find(c)] == False:
#                     flags[brackets_left.find(c)] = True
        
#         for f in flags:
#             if f == False:
#                 return False
#         return True
