for _ in range(int(input())):
    X, Y = map(int, input().split())
    if X == Y or X==0 and Y%2==0 or Y==0 and X%2==0:
        print("YES")
    else:
        print("NO")