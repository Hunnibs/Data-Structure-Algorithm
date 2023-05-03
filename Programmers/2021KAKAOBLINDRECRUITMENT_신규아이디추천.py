def solution(new_id):
    answer = ''

    for word in new_id:
        if len(answer) == 15:
            break

        if 65 <= ord(word) <= 90:
            word = chr(ord(word) + 32)
            answer += word
        elif 97 <= ord(word) <= 122:
            answer += word
        elif 48 <= ord(word) <= 57:
            answer += word
        elif word == '-' or word == '_':
            answer += word
        elif word == '.':
            if not answer or answer[-1] == '.':
                continue
            else:
                answer += word

    for i in range(len(answer) - 1, -1, -1):
        if answer[i] == '.':
            answer = answer[:i]
            print(answer)
        else:
            break

    while len(answer) <= 2:
        if not answer:
            answer += 'a'
        else:
            answer += answer[-1]

    return answer