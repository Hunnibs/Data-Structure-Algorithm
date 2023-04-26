def solution(dartResult):
    answer = 0

    cnt = 0  # 몇 번째 판인지 카운트해줄 변수
    score = ''  # 점수 기록
    result = [0 for _ in range(4)]
    for info in dartResult:
        # 옵션
        if info == '*':
            # 첫 판일 때
            if cnt == 1:
                result[cnt] = result[cnt] * 2
            else:
                result[cnt] = result[cnt] * 2
                result[cnt - 1] = result[cnt - 1] * 2
        elif info == '#':
            result[cnt] = -(result[cnt])

            # 보너스
        elif info == 'S':
            cnt += 1
            result[cnt] = int(score)
            score = ''
        elif info == 'D':
            cnt += 1
            result[cnt] = int(score)
            score = ''
            result[cnt] = result[cnt] ** 2
        elif info == 'T':
            cnt += 1
            result[cnt] = int(score)
            score = ''
            result[cnt] = result[cnt] ** 3

        # 점수
        else:
            score += info

    for i in range(1, 4):
        answer += result[i]

    return answer