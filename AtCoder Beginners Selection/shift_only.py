_ = input()
list_a = [int(i) for i in input().split()]

max_ = 2 ** 9
for a in list_a:
    i = 0
    while a % 2 == 0:
        a /= 2
        i += 1
    if i < max_:
        max_ = i
print(max_)
