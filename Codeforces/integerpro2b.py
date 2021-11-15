for _ in range(int(input())):
    a, b = map(int, input().split())
    diff = abs(a-b)
    if diff == 0:
        print(0)
    else:
        if diff % 10 == 0:
            print(diff//10)
        else:
            c = 0
            while diff > 10:
                rem = diff % 10
                num = diff - rem
                fact = num//10
                diff -= 10*fact
                c+=fact
            print(c+1)