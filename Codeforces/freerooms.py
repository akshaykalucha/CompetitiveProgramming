free = 0
for _ in range(int(input())):
    p, c = map(int, input().split())
    if c-p>=2:
        free+=1
print(free)