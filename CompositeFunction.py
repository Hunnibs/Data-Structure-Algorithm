def CompositeFunction(x, k):
	value = x
	for i in range(k):
		value = Func[value]
	return value

# 입력
n = int(input())

Func = list(map(int, input().split()))
Func.insert(0,0)
q = int(input())

for i in range(q):
	x, k = map(int, input().split())
	print(CompositeFunction(x, k))