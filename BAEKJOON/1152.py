A = input()
B = A.split(' ')
result = len(B)
if A[0] == ' ':
    result -= 1
if A[-1] == ' ':
    result -= 1
    
print(result)