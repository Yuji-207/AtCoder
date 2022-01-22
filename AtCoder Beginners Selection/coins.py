a = int(input())
b = int(input())
c = int(input())
x = int(input())

n500 = x // 500
if c < n500:
    n500 = c

n100 = n500 // 100
if b < n100:
    n100 = b

n50 = n100 // 50
if a < n50:
    n50 = a

if n500 * 500 + n100 * 100 + n50 * 50 !== x:
    print(0)
else:
    i = 5
