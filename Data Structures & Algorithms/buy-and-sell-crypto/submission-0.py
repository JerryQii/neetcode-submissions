class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        left, right = 0, 0
        while right != len(prices) - 1:
            if prices[right] < buy:
                buy = prices[right]
                left = right
            right += 1
            tprofit = prices[right] - buy
            profit = max(profit, tprofit)
        return profit
