class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = prices[0]

        for val in prices:
            maxP = max(maxP, val - minP)
            minP = min(minP, val)

        return maxP