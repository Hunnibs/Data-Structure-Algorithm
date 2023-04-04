def solution(s, n):
    answer = ''
    for spell in s:
        num = ord(spell)
        if 65 <= num and num <= 90:
            if num + n > 90:
                num = num + n - 26
            else:
                num = num + n
        elif 97 <= num and num <= 122:
            if num + n > 122:
                num = num + n - 26
            else:
                num = num + n
        answer += chr(num)

    return answer