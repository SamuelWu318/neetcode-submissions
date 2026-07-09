class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f = 1
        l = 0
        profit = 0
        while f < len(prices):
            poten = prices[f] - prices[l]
            if poten < 0:
                l = f
            f += 1
            profit = max(profit, poten)
        
        return profit