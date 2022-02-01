# first get all non zero elements to beginning of array then add zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non0 = 0
        for num in nums:
            if num != 0:
                nums[non0] = num
                non0 += 1
        for i in range(non0, len(nums)):
            nums[i] = 0
