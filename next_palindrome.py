from sys import argv, exit


def palindrome_number(nbr: str) -> int:
    try:
        int(nbr)
    except Exception:
        return 0
    r_nbr = "".join(reversed(nbr))
    if r_nbr == nbr:
        return 1
    return 0


def next_palindrome(nbr):
    try:
        nb = int(nbr)
    except BaseException:
        print()
        exit(0)

    while True:
        nb += 1
        if palindrome_number(str(nb)):
            print(nb)
            exit(0)


if __name__ == "__main__":
    if len(argv) != 2:
        print()
        exit()

    next_palindrome(argv[1])
