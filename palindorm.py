from sys import argv, exit


def palindorm(str_1):
    s = "".join(reversed(str_1))
    if (s.lower() == str_1.lower()):
        return 1
    return 0


if __name__ == "__main__":
    if len(argv) != 2:
        print()
        exit(0)

    if palindorm(argv[1]):
        print("Palindrome")
    else:
        print("Not palindrome")
