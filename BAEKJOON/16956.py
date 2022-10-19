def fence(pasture, i, j):
    # 늑대 주변에 양이 있는 경우
    if pasture[i-1][j] == 'S':
        return 0
    if pasture[i][j-1] == 'S':
        return 0
    if pasture[i+1][j] == 'S':
        return 0
    if pasture[i][j+1] == 'S':
        return 0
    
    #늑대 주변에 양이 없는 경우
    pasture[i-1][j] == 'D'
    pasture[i][j-1] == 'D'
    pasture[i+1][j] == 'D'
    pasture[i][j+1] == 'D'

R, C = map(int, input().split())
pasture = [input() for _ in range(R)]

for i in range(R):
    for j in range(C):
        if pasture[i][j] == 'W':
            fence(pasture, i, j)