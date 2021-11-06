for _ in range(int(input())):
    X, Y = map(int, input().split())
    two = Y*2
    if (X+two) % 2 == 0:
        print("YES")
    else:
        print("NO")