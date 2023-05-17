def sol(cnt, C):
    if cnt == 0:
        tmp = []
        for i in range(len(answer)):
            tmp.append(str(answer[i]))
        for i in range(C, len(nums)):
            tmp.append(str(nums[i]))

        result.append(''.join(tmp))

        return

    while max(nums) == nums[C]:
        answer.append(nums[C])
        nums[C] = -1
        C += 1

        if C == len(nums):
            break

    if C == len(nums):
        if cnt % 2 == 0 or status:
            tmp = []
            for i in range(len(answer)):
                tmp.append(str(answer[i]))
            result.append(''.join(tmp))
        else:
            tmp = answer[-1]
            answer[-1] = answer[-2]
            answer[-2] = tmp
            tmp = []
            for i in range(len(answer)):
                tmp.append(str(answer[i]))
            result.append(''.join(tmp))

        return

    maxNum = max(nums)

    for i in range(len(nums)):
        if nums[i] == maxNum:
            nums[i] = nums[C]
            nums[C] = -1
            answer.append(maxNum)
            sol(cnt-1, C+1)
            answer.pop()
            nums[C] = nums[i]
            nums[i] = maxNum

T = int(input())
for t in range(1, T+1):
    result = []
    answer = []

    nums, cnt = input().split(' ')

    cnt = int(cnt)
    nums = list(nums)
    for i in range(len(nums)):
        nums[i] = int(nums[i])

    status = 0
    # 중복 Status
    if len(set(nums)) != len(nums):
        status = 1

    sol(cnt, 0)

    ans = 0
    while not ans:
        if len(max(result)) != len(nums):
            result[result.index(max(result))] = ''
        else:
            ans = max(result)

    print('#' + str(t), ans)