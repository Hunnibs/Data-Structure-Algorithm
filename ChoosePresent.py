'''
가치-가격표의 최대 차이가 최소가 되는 상품을 찾기 위해서 정렬을 해주면 0번 인덱스와 n-1번 인덱스의 차이가 가장 최대가 된다. 그렇게 크로스로 비교하고 출력해주면 된다.
시간 복잡도는 정렬하는데 걸리는 시간인 NlogN만큼 2번에 상수시간 연산이 필요하므로 정리하면 O(NlogN)이 걸린다는 것을 알 수 있다. 
'''

n = int(input())

price = list(map(int, input().split()))
weight = list(map(int, input().split()))

price.sort()
weight.sort()

a = weight[n-1] - price[0]
b = price[n-1] - weight[0]

if a >= b:
	print(price[0])
else:
	print(price[n-1])