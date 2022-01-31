#Approach: recalculate maximum price value everytime minimum price is changed
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_so_far = prices[0]
        max_diff_so_far = 0
        for i in range(1, len(prices)):
            if prices[i] > max_so_far:
                max_so_far = prices[i]
            if prices[i] < min_so_far:
                min_so_far = prices[i]
                max_so_far = prices[i]
            if max_so_far - min_so_far > max_diff_so_far:
                max_diff_so_far = max_so_far - min_so_far
        return max_diff_so_far
