'''
n명의 시민이 시장 선거를 했고, 그 결과를 리스트 A에 저장( 1 <= n <= 100,000)
반보다 많은 득표를 해야하고 그렇지 못하면 선거를 다시 실시
후보를 입력 받고 당선자가 있다면 후보자의 번호를 없다면 -1을 출력
'''

'''
표를 받은 후보자 번호만을 저장해주고 후보자 번호 당 표 수를 카운팅 해주는 방식을 사용했다. 
후보자 번호를 저장해주는데 N시간 만큼이 소요, 후보자마다 카운트 시 최악의 경우 모든 후보자를 1표씩 찍는 경우 N * N의 for문에서 시간소요가 걸리기 때문에 Big-O 표기법으로 O(N^2)이다.
'''

# 입력파트
n = int(input())
A = list(map(int, input().split()))
B = []
a = -1

# 후보자 번호만을 저장
for element in A:
	if element not in B:
		B.append(element)

# 후보자마다 카운트
for i in range(0, len(B)):
	if A.count(B[i]) > (n/2):
		a = B[i]
		break

print(a)