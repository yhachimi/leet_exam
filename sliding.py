def sliding_window(nums: list[int], k: int) -> list[int]:
    output: list[int] = []
    for i in range(len(nums) - k + 1):
        tmp = 0
        lst = []
        while tmp < k:
            lst.append(nums[tmp + i])
            tmp += 1
        output.append(max(lst))

    return output


print(sliding_window([1, 2, 3, 4, 1, 5, 1, 6, 0, 2], 2))
