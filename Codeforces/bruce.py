n = int(input())
for i in range(1, n+1):
    if n == 1:
        print("I hate it", end="")
    else:
        if i == 1:
            print("I hate that", end="")
        elif i == n and i%2==0:
            print(" I love it", end="")
        elif i == n and i%2!=0:
            print(" I hate it", end="")
        else:
            if i % 2 == 0:
                print(" I love that", end="")
            else:
                print(" I hate that", end="")