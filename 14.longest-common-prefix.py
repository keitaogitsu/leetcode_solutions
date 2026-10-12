#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_strlen = min(len(s) for s in strs)
        for i in range(min_strlen):
            c = strs[0][i]
            for s in strs:
                if c != s[i]:
                    return strs[0][:i]
        return strs[0][:min_strlen]
# @lc code=end
# --- 最終版の考え方と手順 ---
# 【考え方】
# 共通接頭辞は、全単語で同じ位置の文字が一致している間だけ続く。
# なので strs[0] を基準に、1文字目から順に全単語と比べ、最初の不一致で打ち切る。
# 【手順】
# 1. min_strlen = 最短の単語の長さを求める(これを超えると範囲外アクセスになるため)。
# 2. i を 0 〜 min_strlen-1 まで動かす(位置のループ)。
# 3. 基準 c = strs[0][i] を決める。
# 4. 全単語 s について s[i] と c を比べる(単語のループ)。
# 5. 1つでも違えば、i 文字目の手前までが接頭辞なので strs[0][:i] を返す。
# 6. 最後まで不一致がなければ、最短の単語がそのまま接頭辞なので strs[0][:min_strlen] を返す。

# --- 最初に書いたコード(動かない版) ---
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         pref_chars = []
#         for i in range(len(strs)):
#             for str in strs[i]:
#                 if i == 0:
#                     min_strlen = len(str)
#                 else:
#                     if i != len(strs) and min_strlen > len(str):
#                         min_strlen = len(str)
#         for i in range(min_strlen):
#             chr = strs[0][i]
#             for str in strs:
#                 while chr == str[i]:
#                     if str == strs[len(strs) - 1]:
#                         pref_chars.append(chr)
#         result = ""
#         for char in pref_chars:
#             result += char
#         return result

# --- 最初のコードの振り返り ---
#
# 【いい点】
# - 「最小の長さまでしか比べない」という方針は正しい(範囲外アクセスを防げる)。
# - 「strs[0] の i 文字目を基準に、全単語と比べる」という考え方も正しい。
#   最終版もこの方針のまま。
# - 二重ループで「位置 → 全単語」の順に比べる構造が作れていた。
#
# 【ダメな点 → 直し方】
# 1. 最小長の求め方が違う
#    `for str in strs[i]` は文字列を1文字ずつ回すので、len(str) は常に1になる。
#    また、外側の for i は不要で、同じ処理をn回繰り返していた。
#    → min_strlen = min(len(s) for s in strs) の1行で求める。
#
# 2. while が無限ループになる
#    while の中で chr / str / i が変わらないため、条件が真なら抜けられない。
#    → 「一致している間ループ」ではなく、for の中で if で不一致を見る。
#
# 3. 不一致になっても止まらない
#    共通接頭辞は最初の不一致で終わるのに、打ち切る処理がなかった。
#    → 不一致になった時点で return strs[0][:i] する。
#
# 4. 「最後の単語か」を値の比較で判定している
#    str == strs[len(strs) - 1] は、同じ文字列が重複していると誤判定する。
#    → そもそも判定は不要。不一致で早期 return する形にすれば要らない。
#
# 5. 全部一致したときの戻り値がない
#    最後まで不一致がないと None が返る(["a", "a"] など)。
#    → ループの後に return strs[0][:min_strlen] を置く。
#
# 6. 組み込み名 str / chr を変数名にしている
#    上書きされ、後で str() や chr() が使えなくなる。
#    → s、c など別の名前にする。
#
# 7. 結果の組み立てが遠回り
#    文字をリストに貯めて、1文字ずつ連結している。
#    → スライス strs[0][:i] で、接頭辞をそのまま取り出せる。
#
# 【学んだこと】
# - 「最初の不一致で打ち切る」問題は、早期 return で書くと簡単になる。
# - 空文字などの境界は、特別な分岐を足さず、スライスで自然に処理できる。



