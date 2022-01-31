#Question: https://leetcode.com/problems/jump-game/
#Approach: Assume you can reach the last index and iterate backwards to keep going to the position reachable from current index, check in the end if the current position is the first position

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= can_reach - i:
                can_reach = i
        return can_reach == 0
