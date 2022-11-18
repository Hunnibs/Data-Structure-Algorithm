import sys

n = int(input())
list = []
for _ in range(n):
    list.append(int(sys.stdin.readline()))

list.sort()

for i in range(n):
    print(list[i])
