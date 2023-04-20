def solution(routes):
    answer = 0
    install = [0 for _ in range(len(routes))]

    routes = sorted(routes, key=lambda x: x[0])

    for i in range(len(routes) - 1, -1, -1):
        if install[i]:
            continue

        install[i] = 1
        spot = routes[i][0]
        for j in range(i - 1, -1, -1):
            if routes[j][0] <= spot <= routes[j][1]:
                install[j] = 1
            else:
                break
        answer += 1

    return answer