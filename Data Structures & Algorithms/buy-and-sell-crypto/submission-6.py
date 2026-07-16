class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyday = 0
        sellday = 1
        profit = 0
        while sellday < len(prices):
            potential = prices[sellday] - prices[buyday]
            if potential < 0:
                buyday = sellday
            sellday += 1
            profit = max(profit, potential)

        return profit

