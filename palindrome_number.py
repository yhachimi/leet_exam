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


if __name__ == "__main__":
    if len(argv) != 2:
        print("Not palindrome")
        exit()

    if palindrome_number(argv[1]):
        print("Palindrome")
    else:
        print("Not palindrome")
