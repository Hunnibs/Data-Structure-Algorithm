M, N = map(int, input().split())

dec = [2]
if N >= 3:
    for i in range(M, N+1):
        for num in dec:
            if i % num == 0:
                break

            if num == dec[-1]:
                dec.append(i)

for num in dec:
    print(num)