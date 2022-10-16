A = []
B = []

while True:
    tmp = input()
    if tmp == '0':
        break
    else:
        A.append(tmp)
        B.append(tmp[::-1])
            
for i in range(len(A)):
    if A[i] == B[i]:
        print("yes")
    else:
        print("no")