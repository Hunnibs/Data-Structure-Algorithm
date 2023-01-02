# input
N, M = map(int, input().split())

dic = {}
for _ in range(N):
    url, password = input().split()
    dic[url] = password
    
# output
for _ in range(M):
    url = input()
    print(dic[url])
    