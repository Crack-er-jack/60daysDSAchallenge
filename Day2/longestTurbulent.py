# needs more revision
class Solution:
    def cmp(self, x, y):
        if x > y:
            return 1
        if x < y:
            return -1
        return 0
    def maxTurbulenceSize(self, A):
        N = len(A)
        ans = 1
        anchor = 0

        for i in range(1, N):
            c = self.cmp(A[i-1], A[i])
            if c == 0:
                anchor = i
            elif i == N-1 or c * self.cmp(A[i], A[i+1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
