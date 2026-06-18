def intresection(nbr1: list[int], nbr2: list[int]):
    seens = set(nbr1)
    nb2 = set(nbr2)
    return [n for n in nb2 if n in seens]


if __name__ == "__main__":
    print(intresection([1, 4, 3, 1, 2, 4, 2], [
          1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
