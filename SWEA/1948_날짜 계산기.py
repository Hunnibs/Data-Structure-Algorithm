T = int(input())
for t in range(1, T+1):
    startMonth, startDay, endMonth, endDay = map(int, input().split())

    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = 0

    if startMonth != endMonth:
        for m in range(startMonth, endMonth):
            answer += month[m]

    answer += endDay-startDay+1

    print('#' + str(t), answer)