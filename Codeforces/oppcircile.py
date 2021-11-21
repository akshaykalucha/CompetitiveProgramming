for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a > b:
        a, b = b, a
    gap = b-a
    if b > gap*2 or a > gap or c > gap*2:
        print(-1)
        continue
    if c > gap:
        print(c-gap)
    else:
        print(c+gap)