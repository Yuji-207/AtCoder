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
    
    while s:
        if s[0] == 'a':
            s = s[1:]
        else:
            break

    while s:
        if s[-1] == 'a':
            s = s[:-1]
        else:
            break

    while s:
        if s[0] == s[-1]:
            s = s[1:-1]
        else:
            print('No')
            return None

    print('Yes')
    return None


if __name__ == '__main__':
    s = input()
    main(s)
