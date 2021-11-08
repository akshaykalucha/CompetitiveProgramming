for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    odd = 0
    for num in ll:
        if num%2!=0:
            odd += 1
    if odd == 0 or odd == 1:
        print(0)
    elif odd == 2:
        print(1)
    else:
        print((odd-1)//2)