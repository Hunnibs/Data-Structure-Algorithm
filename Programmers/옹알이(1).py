def solution(babbling):
    answer = 0

    for word in babbling:
        while word:
            if word[:2] in pronounce:
                word = word[2:]

            elif word[:3] in pronounce:
                word = word[3:]

            else:
                break

        if not word:
            answer += 1

    return answer


pronounce = ["aya", "ye", "woo", "ma"]