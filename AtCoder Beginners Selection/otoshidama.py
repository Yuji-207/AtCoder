def main(n, y):
    """
    >>> main(9, 45000)
    4 0 5
    >>> main(20, 196000)
    -1 -1 -1
    >>> main(1000, 1234000)
    14 27 959
    >>> main(2000, 20000000)
    2000 0 0
    >>> main(1, 1000)
    0 0 1
    >>> main(2000, 1000)
    -1 -1 -1
    """

    for i in range(n + 1):
        m = n - i

        for j in range(m + 1):
            k = m - j

            if 10000 * i + 5000 * j + 1000 * k == y:
                print(i, j, k)
                return None

    print(-1, -1, -1)
    return None


if __name__ == '__main__':
    n, y = map(int, input().split())
    main(n, y)
