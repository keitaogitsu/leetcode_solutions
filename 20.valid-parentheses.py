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
# --- 最終版の考え方と手順 ---
# 【考え方】
# 括弧は「直近に開いたものから順に閉じる」必要がある(後入れ先出し)。
# なので開き括弧をスタックに積み、閉じ括弧が来たら一番上と対応しているかを確認する。
# 【手順】
# 1. 閉じ括弧 → 開き括弧の対応辞書 pair_dict を用意する。
# 2. 空のスタック bracket_stack を用意する。
# 3. s を1文字ずつ見る。
#    - 開き括弧(pair_dict.values() に含まれる)なら、スタックに append する。
#    - 閉じ括弧なら、スタックが空、または一番上 bracket_stack[-1] が
#      対応する開き括弧 pair_dict[c] でなければ、return False する。
#      対応していれば pop して、その組を消す。
# 4. 最後までいったら、スタックが空(すべて閉じられた)なら True、残っていれば False。
#    → return len(bracket_stack) == 0

# --- 最初に書いたコード(動かない版) ---
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

# --- 最初のコードの振り返り ---
#
# 【いい点】
# - 「括弧の種類ごとに開き/閉じを対応づけて管理する」という方針は、最終版の対応辞書につながっている。
# - 問題を自分の言葉で分解し、方針をコメントに残せていた。
#
# 【ダメな点 → 直し方】
# 1. 閉じ括弧の対応がずれている
#    brackets_right = "}])" は brackets_left = "([{" と逆順。
#    閉じ括弧 c に brackets_left.find(c) を使うと、常に -1 が返り、flags[-1](curly)を見てしまう。
#    そのため "()" すら False になり、"{}" だけが偶然通る。
#    → 文字列2本の位置対応に頼らず、辞書 {")": "(", ...} で明示的に対応づける。
#
# 2. フラグでは順序と個数の情報が持てない
#    True/False の2値は「その種類が開いているか」しか表せない。
#    対応のバグを直しても、"(()"(個数が合わない)や "([)]"(閉じる順が違う)を誤判定する。
#    → 「直近に開いたものから閉じる」という順序を持てる、スタックを使う。
#
# 3. 判定を最後にまとめている
#    不正が分かった時点でも最後まで処理を続け、フラグで結果を持ち回っていた。
#    → 不一致の時点で return False する。フラグ変数が要らなくなる。
#
# 4. 書き方が遠回り
#    - 内側の for で1文字ずつ == 比較するより、`c in brackets_left` で足りる。
#    - `== False` は `not f` と書く。最後のループは `all(flags)` でも書ける。
#
# 【途中で詰まった点(スタック版に切り替えたあと)】
# - スタックの一番上は bracket_stack[-1]。[:-1] は「最後を除いたリスト」なので別物。
# - 辞書のキーは閉じ括弧なので、`c in pair_dict` は「閉じ括弧か」を意味する。
#   開き括弧を判定したいなら pair_dict.values() を見る(条件の向きを逆にしていた)。
# - 最後に return を書かないと None が返る。return len(stack) == 0 と1行で書く。
#
# 【学んだこと】
# - 「直近のものから順に対応させる」問題は、スタックの出番。
# - 対応関係は辞書で明示すると、位置のずれのようなバグが入りにくい。
# - 不正が分かったら早期 return。フラグの持ち回しは不要になる。
