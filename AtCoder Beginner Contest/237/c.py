def main(s):
    """
    >>> main('kasaka')
    Yes
    >>> main('atcoder')
    No
    >>> main('php')
    Yes
    >>> main('a')
    Yes
    >>> main('b')
    Yes
    >>> main('a' * (10 ** 6))
    Yes
    """

    from collections import deque

    s = deque(s)  # 双方向リスト

    # 両端のaを削除
    while s:

        if s[-1] == 'a':
            s.pop()
            if s and s[0] == 'a':
                s.popleft()

        else:
            break

    # 回文の確認
    while s:

        if s[0] == s[-1]:
            s.pop()
            if s:
                s.popleft()

        else:
            print('No')
            return None

    print('Yes')
    return None


if __name__ == '__main__':
    s = input()
    main(s)
