def solution(today, terms, privacies):
    answer = []

    year, month, day = map(int, today.split("."))

    dic = {}
    for i in range(len(terms)):
        a, b = terms[i].split()
        b = int(b)
        dic[a] = b

    for i in range(len(privacies)):
        p_day, p_type = privacies[i].split()
        y, m, d = map(int, p_day.split("."))

        plus = dic[p_type]
        # 일자 계산
        if d - 1 == 0:
            d = 28
            m -= 1
        else:
            d -= 1

        # 달 계산
        if plus // 12 > 0:
            y += (plus // 12)
            plus = plus % 12

        if m + plus > 12:
            y += 1
            m = m + plus - 12
        else:
            m = m + plus

        if y < year:
            answer.append(i + 1)
        elif y == year:
            if m < month:
                answer.append(i + 1)
            elif m == month:
                if d < day:
                    answer.append(i + 1)

    return answer

