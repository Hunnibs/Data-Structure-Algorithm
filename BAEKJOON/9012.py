def sol(PS):
    arr = []
    for prt in PS:
        if not arr:
            arr.append(prt)
            continue
        # 쌍을 이루는 경우
        if arr[-1] == '(' and prt == ')':
            arr.pop()
        else:
            arr.append(prt)

    return arr

# input
N = int(input())

# main
for _ in range(N):
    PS = input()
    result = sol(PS)

    if result:
        print("NO")
    else:
        print("YES")