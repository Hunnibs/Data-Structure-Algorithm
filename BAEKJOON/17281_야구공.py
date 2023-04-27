import sys
from collections import deque

def play(batting):
    global out_cnt
    global score

    if batting == 0:
        out_cnt += 1
    elif batting == 1:
        for i in range(len(plate)):
            plate[i] += 1
            if plate[i] >= 4:
                plate.popleft()
                score += 1
        plate.append(1)
    elif batting == 2:
        for i in range(len(plate)):
            plate[i] += 2
            if plate[i] >= 4:
                plate.popleft()
                score += 1
        plate.append(2)
    elif batting == 3:
        for i in range(len(plate)):
            plate[i] += 3
            if plate[i] >= 4:
                plate.popleft()
                score += 1
        plate.append(3)
    else:
        while plate:
            plate.popleft()
            score += 1
        score += 1

# input
input = sys.stdin.readline

N = int(input())
player = []
for _ in range(N):
    player.append(list(map(int, input().split())))

# main
batting_order = [0 for _ in range(10)]
batting_order[4] = 0

plate = deque()
score = 0

for i in range(N):
    out_cnt = 0
    while out_cnt != 3:

