class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = prices[0]

        min = 10000
        max = -1

        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
                max = prices[i]

            if prices[i] > max:
                max = prices[i]

        
        return max - min