A = list(input().split())

result = ''
for i in range(8):
	result += A[i]

if result == '12345678':
	print('ascending')
elif result == '87654321':
	print('descending')
else:
	print('mixed')
