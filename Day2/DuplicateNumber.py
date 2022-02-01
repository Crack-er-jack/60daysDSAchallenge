# Floyd's algorithm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t = 0
        h = 0
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if h == t:
                break
        h = 0
        while True:
            t = nums[t]
            h = nums[h]
            if h == t:
                return h
