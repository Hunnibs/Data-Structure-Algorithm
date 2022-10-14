A = int(input())
B = int(input())
C = int(input())

num = str(A*B*C)

for i in range(10):
    cnt = 0 
    i = str(i)
    for j in num:
        if j == i:
            cnt += 1
    print(cnt)