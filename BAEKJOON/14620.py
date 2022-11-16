def sol(sum, cnt):
    global result
    
    if cnt == 3:
        result.append(sum)
        return
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            if check[i][j] or check[i-1][j] or check [i+1][j] or check[i][j-1] or check[i][j+1]:  # 심을 수 없는 경우
                continue
            else:  # 심었을 경우
                sum += tile[i][j] + tile[i-1][j] + tile[i+1][j] + tile[i][j-1] + tile[i][j+1]
                check[i][j] = 1
                check[i][j+1] = 1
                check[i][j-1] = 1
                check[i-1][j] = 1
                check[i+1][j] = 1
                cnt += 1
                
                sol(sum, cnt)
                
                sum -= (tile[i][j] + tile[i-1][j] + tile[i+1][j] + tile[i][j-1] + tile[i][j+1])
                check[i][j] = 0
                check[i][j+1] = 0
                check[i][j-1] = 0
                check[i-1][j] = 0
                check[i+1][j] = 0
                cnt -= 1
        
# input
n = int(input())
tile = [list(map(int, input().split())) for _ in range(n)]

check = []
for i in range(n):
    check.append([])

for i in range(n):
    for j in range(n):
        check[i].append(0)

cnt = 0
sum = 0
result = []
sol(sum, cnt)
print(min(result))