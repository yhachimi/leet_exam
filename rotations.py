def is_rotations(arr, arr2):
    if len(arr) != len(arr2) or sorted(arr) != sorted(arr2):
        return False

    tmp = arr2[:]
    for i in range(len(arr)):
        d = tmp.pop()
        tmp.insert(0, d)
        if tmp == arr:
            return True

    return False


a = [1, 2, 3, 4, 5]
b = [4, 3, 5, 1, 2]
print(is_rotations(a, b))
