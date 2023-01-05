# input
N = int(input())

# main
cnt = 1

for i in range(N, 0, -1):
    cnt = cnt * i

arr = list(map(int, str(cnt)))
arr.reverse()

cnt = 0
for num in arr:
    if num == 0:
        cnt += 1
    else:
        break
print(cnt)
