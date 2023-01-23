#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # m, n = len(img), len(img[0])
        # res = [[0 for _ in range(n)] for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         nums = []
        #         for x in range(max(i - 1, 0), min(m - 1, i + 1) + 1):
        #             for y in range(max(j - 1, 0), min(n - 1, j + 1) + 1):
        #                 nums.append(img[x][y])
        #         res[i][j] = sum(nums) // len(nums)
        # return res

        # 版本2: 前缀和
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i, j in product(range(1, m + 1), range(1, n + 1)):
            presum[i][j] = (
                presum[i - 1][j]
                + presum[i][j - 1]
                - presum[i - 1][j - 1]
                + img[i - 1][j - 1]
            )

        for x, y in product(range(m), range(n)):
            left, right = max(y - 1, 0), min(y + 1, n - 1)
            top, bottom = max(x - 1, 0), min(x + 1, m - 1)

            cnt = (right - left + 1) * (bottom - top + 1)
            total = (
                presum[bottom + 1][right + 1]
                - presum[bottom + 1][left]
                - presum[top][right + 1]
                + presum[top][left]
            )
            ans[x][y] = total // cnt
        return ans


# @lc code=end
