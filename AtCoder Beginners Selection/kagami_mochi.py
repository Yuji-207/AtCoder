def main(n, d):
    """
    >>> main(4, [10, 8, 8, 6])
    3
    >>> main(3, [15, 15, 15])
    1
    >>> main(7, [50, 30, 50, 100, 50, 80, 30])
    4
    >>> main(1, [1])
    1
    >>> main(100, list(range(1, 101)))
    100
    """

    # print(len(set(d)))  # これだけでもOK
    
    count = 0  # 鏡餅の段数

    i = 0
    while i < n:

        count += 1

        j = i + 1
        while j < n:

            if d[i] == d[j]:
                del d[j]  # 同じ直径の鏡餅を削除
                n -= 1
            else:
                j += 1

        i += 1

    print(count)


if __name__ == '__main__':
    n = int(input())
    d = [int(input()) for _ in range(n)]
    main(n, d)
