for _ in range(int(input())):
    a, b = map(int, input().split())
    if a%b==0:
        print(0)
    else:
        if b > a:
            print(b-a)
        else:
            print(b-(a%b))