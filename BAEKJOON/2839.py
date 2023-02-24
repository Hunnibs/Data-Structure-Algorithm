N = int(input())

x = N // 5
y = -1
rest = 0
for i in range(x, -1, -1):
    rest = N - (5 * i)
    if rest % 3 == 0:
        x = i
        y = rest // 3
        break

if y == -1:
    print(y)
else:
    print(x+y)