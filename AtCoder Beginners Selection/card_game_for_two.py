def main(n, a):
    """
    >>> main(2, [3, 1])
    2
    >>> main(3, [2, 7, 4])
    5
    >>> main(4, [20, 18, 2, 18])
    18
    """

    a = sorted(a, reverse=True)  # 数が大きい順にカードをソート

    diff = 0 # 点差
    for i in range(n):
        # 奇数番目で加算し、偶数番目で減算する
        # diff += a[i] * (-1) ** (i % 2)  # 遅い
        if i % 2 == 0:
            diff += a[i]
        else:
            diff -= a[i]

    print(diff)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    main(n, a)
