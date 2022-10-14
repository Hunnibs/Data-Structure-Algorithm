N, M = map(int, input().split())
chess = []
counting = []
cnt = 0 

for _ in range(N):
    chess.append(input())

for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for x in range(i, i+8):
            if (x%2) == 0:
                start = "W"
            else:
                start = "B"
            for y in range(j, j+8):
                if chess[x][y] != start:
                    cnt += 1
                
                if start == "W":
                    start = "B"
                else:
                    start = "W"
        counting.append(cnt)
        

for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for x in range(i, i+8):
            if (x%2) == 0:
                start = "B"
            else:
                start = "W"
            for y in range(j, j+8):
                if chess[x][y] != start:
                    cnt += 1
                
                if start == "W":
                    start = "B"
                else:
                    start = "W"
        counting.append(cnt)
        
print(min(counting))