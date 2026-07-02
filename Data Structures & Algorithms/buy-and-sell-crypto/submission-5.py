class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = prices[0]

        for price in prices:
            maxP = max(maxP, price - minP)
            minP = min(minP, price)
        return maxP