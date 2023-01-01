def GCD():
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd

def LCM():
    i, j = 1, 1
    while(1):
        if a * i == b * j:
            break
        elif a * i < b * j:
            i += 1
        else:
            j += 1

    return a * i

# input
a, b = map(int, input().split())

if b < a:
    tmp = a
    a = b
    b = tmp

# output
print(GCD())
print(LCM())