for _ in range(int(input())):
    X,Y,A,B,K = map(int, input().split())
    if K*A + X > K*B + Y:
        print("DIESEL")
    elif K*A + X == K*B + Y:
        print("SAME PRICE")
    else:
        print("PETROL")