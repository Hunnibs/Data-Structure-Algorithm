N, M = map(int, input().split())
set1 = []
set2 = []
for _ in range(N):
    set1.append(input())

for _ in range(M):
    set2.append(input())

set1 = set(set1)
set2 = set(set2)

result = set1.intersection(set2)
result = list(result)
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])