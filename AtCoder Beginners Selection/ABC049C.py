def main(s):
    """
    >>> main('erasedream')
    YES
    >>> main('dreameraser')
    YES
    >>> main('dreamerer')
    NO
    >>> main('dreamera')
    NO
    >>> main('erase')
    YES
    >>> main('dreamer')
    YES
    >>> main('d')
    NO
    >>> main('d' * 100000)
    NO
    """

    # 文字列の先頭に該当の単語があるかを検証
    while s:

        initial = s[:5]

        # erase or eraser
        if initial == 'erase':
            s = s[5:]

            if s[:1] == 'r':
                s = s[1:]

        # dream or dreamer
        elif initial == 'dream':
            s = s[5:]

            if s[:2] == 'er':
                if not s[:5] == 'erase':  # dreameraserのパターンを除外 対処療法的？
                    s = s[2:]

        else:
            print('NO')
            return None

    print('YES')
    return None
            

if __name__ == '__main__':
    s = input()
    main(s)
