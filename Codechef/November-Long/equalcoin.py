for _ in range(int(input())):
    X, Y = map(int, input().split())
    if X%2!=0 or Y%2!=0:
        print("NO")
    else:
        print("YES")