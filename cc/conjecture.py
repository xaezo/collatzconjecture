def cconjecture(n:int) -> list[int]:
    """Returns a sequence in a form of a python list for n"""

    n = int(n)

    sequence = []

    sequence.append(n)

    while n != 1:
        if n%2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    return sequence

if __name__ == '__main__':
    print(cconjecture(input("Enter an integer: ")))