def main(a, b, c, x):
    """
    >>> from coins import main
    >>> main(2, 2, 2, 100)
    2
    >>> main(30, 40, 50, 6000)
    213
    >>> main(0, 0, 1, 50)
    1
    >>> main(1, 0, 0, 20000)
    0
    """

    n = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if i * 500 + j * 100 + k * 50 == x:
                    n += 1

    print(n)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    main(a, b, c, x)
