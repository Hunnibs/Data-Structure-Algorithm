while(1):
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break

    if x > z and x > y:
        if x ** 2 == ((y ** 2) + (z ** 2)):
            print('right')
        else:
            print('wrong')

    if y > x and y > z:
        if y ** 2 == ((x ** 2) + (z ** 2)):
            print('right')
        else:
            print('wrong')

    if z > x and z > y:
        if z ** 2 == ((x ** 2) + (y ** 2)):
            print('right')
        else:
            print('wrong')