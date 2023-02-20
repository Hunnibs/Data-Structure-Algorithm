def isPalindrome(word):
    return recursion(word, 0, len(word)-1)

def recursion(word, left, right):
    if left >= right:
        return 1
    elif word[left] != word[right]:
        return 0
    else:
        global cnt
        cnt += 1
        return recursion(word, left+1, right-1)

T = int(input())

for _ in range(T):
    word = input()
    cnt = 1
    print(isPalindrome(word), cnt)