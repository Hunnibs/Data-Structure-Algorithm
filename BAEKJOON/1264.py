import sys
import collections

N = int(sys.stdin.readline())
card = collections.deque([i for i in range(1, N+1)])

cnt = 0
while len(card) != 1:
    if cnt == 0:
        card.popleft()
        cnt += 1
    else:
        card.rotate(-1)
        cnt = 0
        
print(card[0])