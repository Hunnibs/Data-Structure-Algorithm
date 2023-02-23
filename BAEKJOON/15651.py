def sol(result):
    if len(result) == M:
        for num in result:
            print(num, end= " ")
        print()
        return

    for i in range(1, N+1):
        result.append(i)
        sol(result)
        result.pop()

N, M = map(int, input().split())

result = []
sol(result)