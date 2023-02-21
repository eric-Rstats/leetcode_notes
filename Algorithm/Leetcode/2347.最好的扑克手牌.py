#
# @lc app=leetcode.cn id=2347 lang=python3
#
# [2347] 最好的扑克手牌
#

# @lc code=start
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        items = ["Flush", "Three of a Kind", "Pair", "High Card"]

        tonghua = max(dict(Counter(suits)).values())
        high_card = max(dict(Counter(ranks)).values())

        if tonghua == 5:
            return "Flush"
        elif high_card >= 3:
            return "Three of a Kind"
        elif high_card >= 2:
            return "Pair"
        else:
            return "High Card"


# @lc code=end
