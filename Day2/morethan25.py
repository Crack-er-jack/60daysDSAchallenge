class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        consec = 0
        for i in range(1, len(arr)):
            if arr[i - 1] == arr[i]:
                consec += 1
                if consec + 1 > len(arr) // 4:
                    return arr[i]
            else:
                consec = 0
        return arr[0]
