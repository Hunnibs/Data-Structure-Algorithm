T = int(input())
Arr = []

for _ in range(T):
    R, S = input().split()
    R = int(R)
    result = ''
    for word in S:
        for _ in range(R):
            result += word
    Arr.append(result)
    
for i in range(T):
    print(Arr[i])