n, m = map(int, input().split())
rem = 6 - max(n,m)
if rem == 0:
    print("1/6")
elif rem == 1:
    print("1/3")
elif rem == 2:
    print("1/2")
elif rem == 3:
    print("2/3")
elif rem == 4:
    print("5/6")
else:
    print("1/1")