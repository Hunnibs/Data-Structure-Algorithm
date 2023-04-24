def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        line = ''
        a, b = arr1[i], arr2[i]
        for j in range(n):
            if a - (2 ** (n - j - 1)) >= 0 or b - (2 ** (n - j - 1)) >= 0:
                line += '#'
            else:
                line += ' '

            if a - (2 ** (n - j - 1)) >= 0:
                a = a - (2 ** (n - j - 1))
            if b - (2 ** (n - j - 1)) >= 0:
                b = b - (2 ** (n - j - 1))
        answer.append(line)

    return answer