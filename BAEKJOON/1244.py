def onoffMan():
    num = number
    i = 2
    while num <= n:
        if switch[num-1] == 0:
            switch[num-1] = 1
        else:
            switch[num-1] = 0
        
        num = number * i
        i += 1

def onoffWoman():
    global number
    number -= 1
    if switch[number] == 0:
        switch[number] = 1
    else:
        switch[number] = 0
        
    i = 1
    while number-i >= 0 and number+i < n and switch[number-i] == switch[number+i]:
        if switch[number-i] == 0:
            switch[number-i] = 1
            switch[number+i] = 1
        else:    
            switch[number-i] = 0
            switch[number+i] = 0
        i += 1  
        
# input
n = int(input())  # 스위치 개수
switch = list(map(int, input().split()))  # 스위치 상태
m = int(input())  # 학생 수
# 학생 성별 & 번호
for _ in range(m):
    gender, number = map(int, input().split())
    if gender == 1:
        onoffMan()
    else:
        onoffWoman()
        
for i in range(len(switch)):
    if i % 20 == 0 and i != 0:
        print()    
        
    print(switch[i], end=" ")