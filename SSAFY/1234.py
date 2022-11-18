def sol():
    stack = []
    stack.append(password.pop(0))
    while(password):
        if stack and stack[-1] == password[0]:
            stack.pop()
            password.pop(0)
        else:
            stack.append(password.pop(0))

    return stack

for i in range(10):
    # input
    n, password = input().split()
    password = list(password)
    stack = sol()

    stack = ''.join(s for s in stack)
    print('#' + str(i+1), stack)