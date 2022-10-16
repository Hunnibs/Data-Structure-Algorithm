import sys

def binary(num, A, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if num == A[m]:
        return 1
    elif num < A[m]:
        return binary(num, A, start, m-1)
    else:
        return binary(num, A, m+1, end)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()
for i in range(M):
	print(binary(B[i], A, 0, N-1))

