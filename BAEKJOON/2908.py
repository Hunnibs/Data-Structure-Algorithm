A, B = input().split()

revA, revB = '', ''
for i in range(2, -1, -1):
    revA += A[i]
    revB += B[i]
revA = int(revA)
revB = int(revB)

if revA > revB:
    print(revA)
else:
    print(revB)