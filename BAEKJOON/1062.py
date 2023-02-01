# 오류 예상 이유: 배울 수 있는 단어 검색 중 alphabet이 들어있는 단어의 개수가 같은 경우 index 상 앞에 있는 것부터 넣으므로 뒤에 있는 index가 더 나은 방법일 경우 error가 발생하는 듯 한다.

# input
N, K = map(int, input().split())  # N: 단어 개수, K: 글자 개수

# 0(a) ~ 26(z)
alphabet = [0] * 26

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    arr = []
    for i in range(N):
        s = set(input())
        s = list(s)
        for word in s:
            if word == 'a':
                continue
            elif word == 'c':
                continue
            elif word == 'n':
                continue
            elif word == 't':
                continue
            elif word == 'i':
                continue
            else:
                alphabet[ord(word)-97] += 1
        arr.append(s)

    for i in range(K-5):
        tmp = alphabet.index(max(alphabet))
        if tmp == 0:
            break

        alphabet[tmp] = 0

        word = chr(tmp+97)
        for j in range(len(arr)):
            if not arr[j].count(word):
                continue
            arr[j].remove(word)

    cnt = 0
    for i in range(len(arr)):
        if len(arr[i]) == 5:
            cnt += 1
    print(cnt)

