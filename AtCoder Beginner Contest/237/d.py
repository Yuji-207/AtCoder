def main(n, s):
    """
    >>> main(5, 'LRRLR')
    1 2 4 5 3 0
    >>> main(7, 'LLLLLLL')
    7 6 5 4 3 2 1 0
    >>> main(5, 'RRRRR')
    0 1 2 3 4 5
    >>> main(1, 'L')
    1 0
    >>> main(1, 'R')
    0 1
    """

    a = [0]  # 先頭の操作を避けるため、出力に対して反転する。
    
    i = 1
    for s_i in s:

        if s_i == 'R':  # 順番が変わらないことが確定した要素を出力して削除
            print(a.pop(), end=' ')
        
        a.append(i)
        i += 1

    print(*a[::-1])


if __name__ == '__main__':
    n = int(input())
    s = input()
    main(n, s)
