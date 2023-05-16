for t in range(1, 11):
    stage = int(input())
    building = list(map(int, input().split()))

    result = 0
    for i in range(2, stage-2):
        if building[i] == 0:
            continue

        comp = building[i-2:i+3]
        top = max(comp)
        if top != building[i] or comp.count(top) > 1:
            continue
        else:
            comp[2] = 0
            result += (top - max(comp))

    print('#' + str(t), result)