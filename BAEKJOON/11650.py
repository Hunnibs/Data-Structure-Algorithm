N = int(input())
arr = []
for _ in range(N):
    arr.append([])

for i in range(N):
    x, y = input().split()
    arr[i].append(int(x))
    arr[i].append(int(y))

arr.sort()

for j in range(N):
    print(arr[j][0], arr[j][1])