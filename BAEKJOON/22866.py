import sys

# input
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

left = [-1 for _ in range(N)]
right = [-1 for _ in range(N)]
count = [0 for _ in range(N)]

stack = []
idx = []
for i in range(N):
    while stack:
        if stack[-1] <= L[i]:
            stack.pop()
            idx.pop()
        else:
            break
    count[i] += len(stack)
    if stack:
        left[i] = idx[-1]
    stack.append(L[i])
    idx.append(i)

stack = []
idx = []
for i in range(N-1, -1, -1):
    while stack:
        if stack[-1] <= L[i]:
            stack.pop()
            idx.pop()
        else:
            break
    count[i] += len(stack)
    if stack:
        right[i] = idx[-1]
    stack.append(L[i])
    idx.append(i)

for i in range(N):
    if count[i] == 0:
        print(0)
    else:
        if left[i] == -1:
            print(count[i], right[i]+1)
        elif right[i] == -1:
            print(count[i], left[i]+1)
        elif i-left[i] <= right[i]-i:
            print(count[i], left[i]+1)
        else:
            print(count[i], right[i]+1)