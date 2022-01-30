def main(n):
    """
    >>> main(-2**31)
    Yes
    >>> main(0)
    Yes
    >>> main(2**31)
    No
    >>> main(-2**63)
    No
    >>> main(2**63)
    No
    """

    comp = 2 ** 31

    if -comp <= n < comp:
        print('Yes')
    else:
        print('No')

s
if __name__ == '__main__':
    n = int(input())
    main(n)
