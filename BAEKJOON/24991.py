# input
T, N = input().split()
D = list(map(int, input().split()))

# main
N = int(N)
Day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for i in range(N):
    if D[i] % 30  == 0 and D[i] != 0:
        D[i] = 0
    elif D[i] > 30 and D[i] % 30 == 1 and T == "Sun":  # 지급을 받는 날이 주말인 경우 다음달로 넘어가는게 아니라 주말이 끝나면 받게 해줌
        D[i] = -1
    else:
        D[i] = 30 - (D[i] % 30)

minNum = min(D)  # 가장 빨리 받을 수 있는 날

if minNum == -1:
    minNum = 1
else:
    tmp = minNum % 7
    idx = Day.index(T)
    pDayIdx = (idx + tmp) % 7  # 현재 요일

    if Day[pDayIdx] == "Sat":
        minNum += 2 
    elif Day[pDayIdx] == "Sun":
        minNum += 1


print(minNum)