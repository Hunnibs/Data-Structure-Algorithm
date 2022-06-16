'''
입력:
n개의 서로 다른 정수 값(첫 줄에 n, 두 번째 줄부터 n개의 정수 값이 줄마다 하나씩)
단, a < b < c 이며 b-a <= c-b <= 2*(b-a)를 만족
출력:
입력 정수 값에서 위 두 조건을 만족하는 (a,b,c) 쌍의 개수
'''

'''
이진분할 알고리즘을 활용 count_by_range함수를 이용하여 a <= b <= 2a 사이 값의 개수를 알아낸다. 
정렬된 수를 순서대로 A, B, C라 했을때 B-A의 값을 x라 하면 B 에서 X 만큼 더 갔을 때부터 2x만큼 더 갔을 때 사이에서 값의 개수를 구하는 방식이다.
시간복잡도는 sort함수가 logN만큼의 시간, 반복문에서 (n-1)(n-2) / 2 * logN으로(기본 상수연산은 제외하였음) 시간복잡도는 Big-O 표기법으로 O(n^2)으로 표시된다. 
'''
from bisect import bisect_right, bisect_left

def count_by_range(a, left_value, right_value):  # 이진분할 알고리즘 활용  
    rindex = bisect_right(a, right_value)
    lindex = bisect_left(a, left_value)
    return rindex-lindex

n = int(input())
A = [int(input()) for _ in range(n)]

A.sort()  # 알고리즘 사용을 위한 정렬

count = 0
Max = A[n-1]

for i in range(0, n-1):
	for j in range(i+1, n):
		left = A[j] + (A[j] - A[i])  # left 값은 A[j]-A[i]를 A[j]에서 더해준 값
		right = A[j] + (A[j] - A[i]) * 2  # right 값은 A[j] - A[i]의 두 배를 A[j]에 더해준 값
		if right > Max:  # 입력받은 값의 최대보다 더 크다면 오류가 발생함
			if (A[j] - A[i]) > (Max - A[j]):  # 사이에 값이 없는 경우
				break
			else:
				right = Max
		if count_by_range(A, left, right) > 0:  # 값
			count += count_by_range(A, left, right)

print(count)