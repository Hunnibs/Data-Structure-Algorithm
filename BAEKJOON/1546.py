N = int(input())
A = list(map(int, input().split()))

M = max(A)
sum = 0

for i in range(len(A)):
    A[i] = round(A[i]/M * 100, 2)
        
for i in range(len(A)):
    sum += A[i]
    
print(sum/N)