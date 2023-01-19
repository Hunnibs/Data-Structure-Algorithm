def solution(survey, choices):
    id = ["R", "T", "C", "F", "J", "M", "A", "N"]
    score = [0, 0, 0, 0, 0, 0, 0, 0]

    # 점수 계산 루프문
    for i in range(len(choices)):
        if choices[i] == 4:  # 모르겠다 선택지
            continue

        a, b = id.index(survey[i][0]), id.index(survey[i][1])

        if choices[i] == 1:
            score[a] += 3
        elif choices[i] == 2:
            score[a] += 2
        elif choices[i] == 3:
            score[a] += 1
        elif choices[i] == 5:
            score[b] += 1
        elif choices[i] == 6:
            score[b] += 2
        elif choices[i] == 7:
            score[b] += 3

    # 유형결정
    answer = ''
    num = 0
    for _ in range(4):
        if score[num] >= score[num+1]:
            answer += id[num]
        else:
            answer += id[num+1]

        num += 2

    return answer