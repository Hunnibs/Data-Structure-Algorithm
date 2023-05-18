T = int(input())
for t in range(1, T+1):
    answer = 0

    N, K = map(int, input().split())
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))

    for x in range(N):
        cnt = 0
        for y in range(N):
            if puzzle[x][y] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1

                cnt = 0

        if cnt == K:
            answer += 1


    for y in range(N):
        cnt = 0
        for x in range(N):
            if puzzle[x][y] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1

                cnt = 0

        if cnt == K:
            answer += 1

    print('#' + str(t), answer)