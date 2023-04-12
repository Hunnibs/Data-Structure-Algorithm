import sys

# input
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

# main
card.sort()
result = []

for num in numbers:
    lowIdx, upperIdx = -1, -1
    # lowIdx
    l, r = 0, len(card)-1
    while l <= r:
        mid = (l+r) // 2
        if card[mid] == num:
            lowIdx = mid
            r = mid - 1
        elif card[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    # upperIdx
    l, r = 0, len(card)-1
    while l <= r:
        mid = (l+r) // 2
        if card[mid] == num:
            upperIdx = mid
            l = mid + 1
        elif card[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    if upperIdx == -1:
        result.append(0)
    else:
        result.append(upperIdx-lowIdx+1)

result_str = ' '.join(str(s) for s in result)
print(result_str)