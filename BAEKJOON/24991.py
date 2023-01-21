# input
T, N = input().split()
D = list(map(int, input().split()))

# main
Day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
D.sort()
tmp = (30 - D[-1]) % 7

idx = Day.index(T)
idx += tmp
if idx > 7:
    idx = idx - 7

if Day[idx] == "Sat":
    answer = 30 - D[-1] + 2
elif Day[idx] == "Sun":
    answer = 30 - D[-1] + 1
else:
    answer = 30 - D[-1]

if answer < 0:
    answer = 30 - (answer)

print(answer)