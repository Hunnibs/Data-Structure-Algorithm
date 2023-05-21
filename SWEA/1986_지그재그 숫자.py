T = int(input())
for t in range(1, T+1):
    N = int(input())

    answer = 1
    for i in range(2, N+1):
        if i % 2 == 0:
            answer -= i
        else:
            answer += i

    print('#' + str(t), answer)