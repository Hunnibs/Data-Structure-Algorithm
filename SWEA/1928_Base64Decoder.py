def decoding(num):
    decode = ''
    for i in range(5, -1, -1):
        if num - (2**i) >= 0:
            decode += '1'
            num = num - (2**i)
        else:
            decode += '0'

    return decode

def translate(sum):
    result = ''

    a = len(sum) // 8
    for i in range(a):
        b = i * 8
        tmp = sum[b:b+8]

        num = 0
        i = 7
        for t in tmp:
            t = int(t)
            num += t * (2**i)
            i -= 1

        result += chr(num)
    return result

T = int(input())
for t in range(1, T+1):
    base = input()
    sum = ''

    for word in base:
        if 48 <= ord(word) <= 57:
            num = ord(word)+4
            sum += decoding(num)

        elif 65 <= ord(word) <= 90:
            num = ord(word)-65
            sum += decoding(num)

        elif 97 <= ord(word) <= 122:
            num = ord(word)-71
            sum += decoding(num)

        elif word == '+':
            num = 62
            sum += decoding(num)

        else:
            num = 63
            sum += decoding(num)
    result = translate(sum)
    print('#' + str(t), result)