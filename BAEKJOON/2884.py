H, M = map(int, input().split())

if (M-45) >= 0:
	print(H, M-45)
else:
	if H-1 >= 0:
		print(H-1, 60+(M-45))
	else:
		print(23, 60+(M-45))