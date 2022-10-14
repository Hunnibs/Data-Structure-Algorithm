arr = []

n = int(input())
for _ in range(n):
	arr.append(input())

for i in range(n):
	sum = 0
	cnt = 1
	for sym in arr[i]:
		if sym == 'O':
			sum += cnt
			cnt += 1
		else:
			cnt = 1
	print(sum)
