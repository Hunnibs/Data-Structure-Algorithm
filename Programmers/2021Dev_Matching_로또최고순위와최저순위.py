def solution(lottos, win_nums):
    answer = []

    # 당첨번호 개수
    count = 0
    for win_num in win_nums:
        if win_num in lottos:
            count += 1

    zero_count = 0
    for num in lottos:
        if not num:
            zero_count += 1

    min_rate = abs(count - 7)
    max_rate = abs(count + zero_count - 7)

    if min_rate > 6:
        min_rate = 6
    if max_rate > 6:
        max_rate = 6

    answer.append(max_rate)
    answer.append(min_rate)

    return answer