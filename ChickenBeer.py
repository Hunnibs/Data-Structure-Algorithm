'''
치킨 집에서 t분 간 치킨과 맥주를 마신다.
후라이트는 a분, 양념은 b분 남은 시간에 맥주를 마신다.
정확히 t분에 맞춰 치킨을 못 먹을 경우 최대한 오래 치킨을 먹고 남은 시간에는 맥주를 마시려고 한다.
'''

'''
함수는 전체시간을 기준으로 먹는 시간이 오래 걸리는 치킨을 먼저 먹고 나머지 시간을 먹는 시간이 짧게 걸리는 치킨으로 채운다. 오래 걸리는 치킨을 0개부터 증가시켜 루프문을 돌면 결과를 구할수 있다
시간 복잡도는 for문 하나만을 사용하기 때문에 O(n)시간 안에 해결이 가능하다. 
'''

def solve(a, b, t):
    # 코드 + 출력
    time_left = a  # 가장 적은 시간이 남았을 때를 계산하기 위한 변수
    count = t // b
    
    for i in range(count+1):
        time = t
        time = time - (b*i)

        if time%a == 0:  # 시간 딱 맞춰서 다 먹는 경우
            if i == 0:
                print (time//a)
                return
            else:
                print(i+time//a)
                return

        if time_left > (time%a):  # 남은 시간이 더 적을 경우만 업데이트
            resultA, resultB = i, time//a
            time_left = time%a
    
    print(resultA+resultB, t-b*resultA-a*resultB)

a, b, t = [int(x) for x in input().split()]
if a < b:  # 후라이드 먹는 시간이 더 짧은 경우
    solve(a, b, t)
else:  # 양념 먹는 시간이 더 짧은 경우
    solve(b, a, t)
