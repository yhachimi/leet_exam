def stars(cords: list[tuple[int, int]], size: int) -> list[str]:
    data = {i: list("." * size) for i in range(size)}
    try:

        for x, y in cords:
            if x >= 0 < size and y >= 0 < size:
                data[x][y] = "*"
        return ["".join(data[i]) for i in range(size)]
    except BaseException:
        return ["".join(data[i]) for i in range(size)]


if __name__ == "__main__":
    print(stars([(0, 2), (0, 0), (-1, 6)], 3))
