class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            mini = float("inf")
            tmp = ""
            for j  in range(i + 1):
                tmp += s[j]
                if tmp == tmp[::1]:
                    cost  = 1 + dp[j + 1]
                    mini = min(cost, mini)
            dp[i] = mini

        return dp[0] - 1
