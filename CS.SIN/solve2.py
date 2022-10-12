n, m = map(int, input().split())
exit = n // 2
permutation = list(map(int, input().split()))
row = [[] for _ in range(n)]
direction = [[] for _ in range(n)]
max_row = 0
for _ in range(m):
	i, j = map(int,input().split())
	row[i].append(j)
	row[i+1].append(j)
	direction[i].append(j)
	if j > max_row:
		max_row = j
move = exit
for i in range(max_row, 0, -1):
	for w in row[exit]:
		if w == i:
			for w in direction[exit]:
				print(direction[exit])
				if w == i:
					move = exit + 1
					break
			if move == exit:
				exit -= 1
				move = exit
			else:
				exit += 1
				move = exit
			break

print(permutation[exit])