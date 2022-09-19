n = int(input())
A = list(map(int, input().split()))
A.sort()
B = []
for i in range(n):
	B.append(A.pop() + A.pop(0))
print(min(B))