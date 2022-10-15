N, K = map(int, input().split())
arr = []
result = []

for i in range(N):
    arr.append(i+1)
    
cnt = 1
while True:
    if cnt != K:
        cnt += 1
        arr.append(arr.pop(0))
    else:
        result.append(arr.pop(0))
        cnt = 1
    if not arr:
        break
        
print('<', end='')

while result:
    print(result.pop(0), end='')
    if result:
        print(', ', end='')
        
print('>')