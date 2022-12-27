def sol(start):
    for i in arr[start]:
        if i == 1:
            continue

        if virus.count(i) == 0:
            virus.append(i)
            sol(i)

# input
N = int(input())
cnt = int(input())

arr = []
for _ in range(N+1):
    arr.append([])

for _ in range(cnt):
    a, b = map(int, input().split())

    arr[a].append(b)
    arr[b].append(a)

virus = []
sol(1)

print(len(virus))