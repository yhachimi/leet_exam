from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        strongest = []
        m = (len(arr) - 1) // 2
        arr = sorted(arr)
        midell = arr[m]
        dct = {n: abs(n - midell) for n in arr}
        arr = sorted(arr, key=lambda x: (dct[x], x), reverse=-True)
        strongest = arr[0:k]
        return strongest


obj = Solution()


print(obj.getStrongest([1, 2, 3, 4, 5], 2))
