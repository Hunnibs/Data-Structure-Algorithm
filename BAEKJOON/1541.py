# input
val = input().split('-')

# main
for i in range(len(val)):
	arr = val[i].split('+')
	sum = 0
	for j in range(len(arr)):
		sum += int(arr[j])
	val[i] = sum

result = val[0]
for i in range(1, len(val)):
	result -= val[i]

print(result)