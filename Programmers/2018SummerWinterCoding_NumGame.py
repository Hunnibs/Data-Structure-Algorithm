from collections import deque


def solution(A, B):
    A.sort()
    B.sort()
    M = deque(A)
    N = deque(B)

    answer = 0
    while (N):
        if M[0] < N[0]:
            M.popleft()
            N.popleft()
            answer += 1
        else:
            N.popleft()

    return answer