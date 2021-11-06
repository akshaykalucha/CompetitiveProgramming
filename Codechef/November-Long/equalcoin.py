for _ in range(int(input())):
    X, Y = map(int, input().split())
    Flag = False
    if (X+(Y*2))%2==1:
        Flag = False
    else:
        Flag = True
        if X==0 and Y%2==1:
            Flag = False
    if Flag == False:
        print("NO")
    else:
        print("YES")