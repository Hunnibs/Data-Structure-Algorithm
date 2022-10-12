'''
트리를 리스트 형식으로 구현 F(x) = value(0 <= x <= n-1)에서 x를 인덱스 값으로 해당 리스트에 value값을 저장
각 질의 당 시간 복잡도는 O(k)만큼 걸린다. 
'''
def CompositeFunction(x, k):  # 계속해서 타고 내려가는 방식
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