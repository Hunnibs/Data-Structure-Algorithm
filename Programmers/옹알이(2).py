def solution(babbling):
    answer = 0
    pronounce = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        tmp = ''
        while word:
            if word[:2] in pronounce and tmp != word[:2]:
                tmp = word[:2]
                word = word[2:]

            elif word[:3] in pronounce and tmp != word[:3]:
                tmp = word[:3]
                word = word[3:]

            else:
                break

        if not word:
            answer += 1

    return answer

