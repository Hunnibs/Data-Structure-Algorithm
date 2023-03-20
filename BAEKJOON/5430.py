import sys
from collections import deque

def sol():
    global status
    for cmd in p:
        if cmd == "R":
             if status == 0:
                 status = 1
             else:  # status == 1
                 status = 0
        elif cmd == "D":
            if status == 0:
                queue.popleft()
            else:
                queue.pop()

    if status == 1:
        queue.reverse()

# input
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    queue = deque(input().rstrip()[1:-1].split(","))

    count = 0
    for cmd in p:
        if cmd == "D":
            count += 1

    if count > n:
        print("error")
    else:
        status = 0
        sol()
        print('[' + ",".join(queue) + ']')