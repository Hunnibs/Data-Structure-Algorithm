N = int(input())
P = list(map(int, input().split()))
P.sort()

sum = 0
for i in range(N):
    sum += (N * P[i])
    N -= 1
print(sum)