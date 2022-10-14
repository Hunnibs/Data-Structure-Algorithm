A = input()
A = A.upper()
B = list(set(A))

arr = []

for i in B:
    arr.append(A.count(i))

Max = max(arr)
if arr.count(Max) > 1:
    print("?")
else:
    print(B[arr.index(Max)])