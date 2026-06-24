class Solution:
    def minCut(self, s: str) -> int:
        res = []
        path = []
        if s == s[::-1] or not s:
            return 0

        def backtrack(start: int):
            if start == len(s):
                res.append(len(path))
                return

            for end in range(start + 1, len(s) + 1):
                sub = s[start: end]
                if sub == sub[::-1]:
                    path.append(sub)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return min(res) - 1


if __name__ == "__main__":
    obj = Solution()
    print(obj.minCut("abcd"))
