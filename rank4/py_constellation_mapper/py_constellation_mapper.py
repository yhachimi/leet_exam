def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    res = []
    for r in range(size):
        string = ""
        for c in range(size):
            if (r, c) in stars:
                string += '*'
            else:
                string += '.'
        res.append(string)
    return res
