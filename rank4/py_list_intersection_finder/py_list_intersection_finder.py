def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    hashT = {}
    res = []
    for arr in lists:
        for el in arr:
            if el in hashT:
                hashT[el] += 1
            else:
                hashT[el] = 1
    for k, v in hashT.items():
        if hashT[k] >= len(lists):
            res.append(k)
    return sorted(res)
