'''
리스트 A의 값을 오름차순으로 정렬한 후, 실수록 왼쪽 방향으로 몇 번 rotation 이동을 한 상황, 몇번을 회전을 했는지 궁금하다.

입력:
서로 다른 n개의 값을 오름차순으로 정렬 후 k번 왼쪽 회전을 한 리스트 A
출력:
A에 대한 회전 횟수
'''

'''
이진탐색을 이용하여 값이 갑자기 줄어들었을 경우의 인덱스를 찾아주는 방식을 활용하였다.
시간복잡도는 이진탐색을 활용하였으므로 최악의 경우 O(logN)이 나온다.
'''
L = list(map(int, input().split()))

n = len(L)-1
left = 0 
right = n

while right-left >= 0:
	if L[left] < L[right]:  # 오름차순 정렬이 되있을 경우 가장 왼쪽 값이 최솟값 인덱스
		result = left
		break
		
	mid = (right+left) // 2  # 이진탐색
	if L[mid] - L[mid-1] < 0:  # 값이 감소할 경우 감소한 값이 최솟값 인덱스
		result = mid
		break
	
	if L[left] > L[mid]:  # 반으로 나눈 기준 왼쪽에 최솟값이 존재
		right = mid - 1
	else:  # 반으로 나눈 기준 오른쪽에 최솟값이 존재
		left = mid + 1
		
if result == 0:  # 한번도 움직이지 않은 경우
	print(result)
else:
	print(len(L)-result)