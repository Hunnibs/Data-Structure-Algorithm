import sys
from itertools import combinations
from math import inf

# input
input = sys.stdin.readline

N, M = map(int, input().split())

street = []
for _ in range(N):
    street.append(list(map(int, input().split())))

# main
chicken = []
house = []
for x in range(N):
    for y in range(N):
        if street[x][y] == 2:
            chicken.append([x, y])
        elif street[x][y] == 1:
            house.append([x, y])

min_chickenHouse = list(combinations(chicken, M))
result = inf
for i in range(len(min_chickenHouse)):
    total_dist = 0
    for x in range(len(house)):
        r1, c1 = house[x]
        dist = inf
        for y in range(len(min_chickenHouse[i])):
            r2, c2 = min_chickenHouse[i][y]
            dist = min(dist, abs(r1-r2)+abs(c1-c2))
        total_dist += dist
        if total_dist > result:
            break

    if total_dist < result:
        result = total_dist

print(result)