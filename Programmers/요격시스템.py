def solution(targets):
    answer = 0
    N = len(targets)
    visited = [0 for _ in range(N)]

    targets = sorted(targets, key=lambda x: x[0])
    for i in range(N - 1, -1, -1):
        if visited[i]:
            continue
        visited[i] = 1
        for j in range(i - 1, -1, -1):
            if targets[i][0] < targets[j][1]:
                visited[j] = 1
            else:
                break

        answer += 1

    return answer