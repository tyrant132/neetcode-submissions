class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        maxP = 0
        n = len(prices)
        for i in range(n):
            s = prices[i]-curMin
            curMin = min(curMin, prices[i])
            maxP = max(maxP,s)
        return maxP