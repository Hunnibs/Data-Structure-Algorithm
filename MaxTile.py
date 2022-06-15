'''
tile의 가중치 값들을 3개씩 합해 저장해준 이차원 리스트를 생성해준다. 이 후 각 행 별로 max값을 뽑아 Max 리스트를 생성해주고 거기서 Max값을 찾는다.
시간복잡도의 경우 tile 리스트 생성 시 n, maxtile 생성 시 n + n*cnt, maxtile 함수에서 Max함수 생성 시 n, 마지막 연산 시 모든 내장 함수는 n시간 내에 동작 가능하기 때문에 kn시간이 걸린다 
결국 O(n) 시간 안에 해결 가능하다.
'''

def Max_tile():
	if k > n//3 * n:  # 예외조건 처리
		return -1

	Max = []  # 각 행의 Max값 저장
	for i in range(n):
		Max.append(max(maxtile[i]))

	sum = 0
	for i in range(k):
		tmp = max(Max)
		sum += tmp
		idx = Max.index(tmp)
		maxtile[idx].remove(tmp)
		if len(maxtile[idx]) >= 3:  # 3개씩 합쳐놓은게 3개를 넘지 못하면 그 타일에 넣을 수 있는 값을 넘어섰으므로 0으로 초기화
			Max[idx] = max(maxtile[idx])
		else:
			Max[idx] = 0

	return sum

n, k = map(int, input().split())

tile = [list(map(int, input().split())) for _ in range(n)]

cnt = n-3+1
maxtile = []
for i in range(n):  # 이차원 리스트 생성
	maxtile.append([])

for i in range(n):  # 행 별로 계산해야하므로 각 행별 3*1 값 따로 저장
	for j in range(cnt):
		maxtile[i].append(tile[i][j]+tile[i][j+1]+tile[i][j+2])

print(Max_tile())