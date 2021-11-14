for _ in range(int(input())):
    c=int(input())
    if c == 3:
        print(1)
    elif c > 3:
        if c%2==0:
            print((c//2)-1)
        else:
            print((c-1)//2)
    else:
        print(0)