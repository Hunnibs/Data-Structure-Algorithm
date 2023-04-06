def solution(numbers, target):
    answer = 0

    answer = dfs(numbers, 0, 0, target, answer)

    return answer


def dfs(numbers, x, result, target, answer):
    if x == len(numbers):
        if result == target:
            answer += 1
        return answer

    for i in range(x, len(numbers)):
        result += numbers[i]
        answer = dfs(numbers, i + 1, result, target, answer)
        result -= 2 * numbers[i]

    if result == target:
        answer += 1
    return answer
