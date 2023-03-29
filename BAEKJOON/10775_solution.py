import sys

def find(x):
    if GL[x] == x:
        return x

    root = find(GL[x])
    GL[x] = root
    return GL[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        GL[y] = x
    else:
        GL[x] = y

# input
input = sys.stdin.readline

G = int(input())
P = int(input())
PL = []
for _ in range(P):
    PL.append(int(input()))

GL = [i for i in range(G+1)]
total = 0
for PNum in PL:
    root = find(PNum)

    if root == 0:
        break
    union(root, root-1)
    total += 1

print(total)