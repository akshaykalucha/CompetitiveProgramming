n, k = map(int, input().split())

mins = 240-k
if mins == 0:
    print(0)
else:
    c = 0
    i=1
    while True:
        if 5*i<=mins and i<=n:
            mins-=5*i
            i+=1
            c+=1
        else:
            break
    print(c)