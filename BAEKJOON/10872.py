def factorial(num):

    # 재귀의 끝에 도달하면 리턴
    if num == 1:
        return 1

    return num * factorial(num-1)

N = int(input())

result = 0
if N == 0:
    print(1)
else:
    print(factorial(N))
