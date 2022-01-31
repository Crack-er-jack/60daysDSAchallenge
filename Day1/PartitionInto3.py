#Question: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
#Approach: find sum of array, if not divisible by 3 answer is false, else see if we can partition the array into 3 parts with same sum
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        arr_sum = sum(arr)
        if arr_sum % 3 != 0:
            return False
        first = 0
        found1 = False
        found2 = False
        second = 0
        for i in range(len(arr)):
            if not found1:
                first += arr[i]
                if first == arr_sum // 3:
                    found1 = True
                    continue
            if found1:
                second += arr[i]
                if second == arr_sum // 3:
                    found2 = True
                    break
        return found1 and found2 and i != len(arr) - 1
