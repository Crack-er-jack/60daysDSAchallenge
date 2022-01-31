#Question: https://leetcode.com/problems/product-of-array-except-self/
#Approach: store the product from beginning and from ending (except the element itself) in two arrays and multiply the values at index to get output array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod_beg = [0] * n
        prod_end = [0] * n
        output = [0] * n
        prod_beg[0] = 1
        prod_end[n - 1] = 1
        for i in range(1, n):
            prod_beg[i] = prod_beg[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            prod_end[i] = prod_end[i + 1] * nums[i + 1]
        for i in range(n):
            output[i] = prod_beg[i] * prod_end[i]
        return output
