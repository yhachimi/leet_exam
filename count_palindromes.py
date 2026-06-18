from sys import argv, exit


def palindorm(str_1):
    s = "".join(reversed(str_1))
    if (s.lower() == str_1.lower()):
        return 1
    return 0


if __name__ == "__main__":
    if (len(argv) == 1):
        print("0")
        exit(0)

    lst_palindorm = argv[1:len(argv)]
    count = 0
    for pld in lst_palindorm:
        if palindorm(pld) == 1:
            count += 1

    print(count)
