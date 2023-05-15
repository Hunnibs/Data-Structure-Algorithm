import sys
from collections import deque

# input
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N = int(input())
    value = list(map(int, input().split()))

    value = deque(value)
    answer = 0
    while value:
        high = max(value)
        idx = value.index(high)
        for _ in range(idx):
            answer += (high - value.popleft())
        value.popleft()

    print('#' + str(t), answer)