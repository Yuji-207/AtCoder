def main(n, s):

    a = [0]
    idx = 0

    for i in range(n):

        if s[i] == 'L':
            # idxはそのまま
            a.insert(i, i + 1)

        else:
            idx += 1
            a.insert(idx, i + 1)

    print(*a)


if __name__ == '__main__':
    n = int(input())
    s = input()
    main(n, s)
