def solution(N, stages):
    answer = []

    users = len(stages)
    clear = stages.count(N + 1)

    result = [-1 for _ in range(N + 1)]
    for stage in range(N, 0, -1):
        fail = stages.count(stage)
        clear += fail
        if clear == 0:
            result[stage] = 0.0
        else:
            result[stage] = fail / clear

    for _ in range(N):
        idx = result.index(max(result))
        answer.append(idx)
        result[idx] = -1
    return answer