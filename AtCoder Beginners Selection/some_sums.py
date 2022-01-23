def main(n, a, b):
    """
    >>> from some_sums import main
    >>> main(20, 2, 5)
    84
    >>> main(10, 1, 2)
    13
    >>> main(100, 4, 16)
    4554
    >>> main(1, 1, 36)
    1
    """

    sum_ = 0
    for i in range(1, n+1):
        s = str(i)
        s = map(int, s)  # 数を桁ごとに分割
        s = sum(s)

        if a <= s <= b:
            sum_ += i

    print(sum_)


if __name__ == '__main__':
    n, a, b = map(int, input().split())
    main(n, a, b)
