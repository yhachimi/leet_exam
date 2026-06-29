def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return [] 
    res = []
    L, R = 0, k
    while R <= len(nums):
        big = max(nums[L:R])
        res.append(big)
        L += 1
        R += 1
    return res
