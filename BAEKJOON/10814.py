# lambda 함수 사용

N = int(input())

arr = []
for i in range(N):
    arr.append(input().split())
    arr[i][0] = int(arr[i][0])

arr.sort(key=lambda x:x[0])

for i in range(N):
    print(arr[i][0], arr[i][1])