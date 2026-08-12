class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1

        res = 0

        while l < r:
            value = prices[l] * prices[r]
            res = max(value, res)

            if prices[l] < prices[r]:
                l += 1
            else: r -= 1

        return res