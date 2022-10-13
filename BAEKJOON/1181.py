N = int(input())

arr = []
for _ in range(N):
	arr.append(input())

arr = set(arr)
arr = list(arr)

arr.sort()
arr.sort(key=len)

for i in range(len(arr)):
	print(arr[i])