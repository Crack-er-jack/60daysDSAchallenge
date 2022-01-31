#Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
#Approach: Use same approach as in BuySell.py, divide the prices into two parts and get maximum profit separately
#Note: Current solution gives TLE, should improve further using dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i in range(len(prices)):
            profits.append(self.maxProfitHalf(prices[:i]) + self.maxProfitHalf(prices[i:]))
        return max(profits)
    def maxProfitHalf(self, hprices: List[int]) -> int:
        if hprices == []:
            return 0
        min_so_far = hprices[0]
        max_so_far = hprices[0]
        max_diff_so_far = 0
        for i in range(1, len(hprices)):
            if hprices[i] > max_so_far:
                max_so_far = hprices[i]
            if hprices[i] < min_so_far:
                min_so_far = hprices[i]
                max_so_far = hprices[i]
            if max_so_far - min_so_far > max_diff_so_far:
                max_diff_so_far = max_so_far - min_so_far
        return max_diff_so_far
