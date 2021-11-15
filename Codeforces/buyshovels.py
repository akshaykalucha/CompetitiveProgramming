k, r = map(int, input().split())
if k%10==0:
    print(1)
else:
    c = 1
    while True:
        curr=k*c
        rem = curr%10
        if rem==0:
            break
        if ((curr-rem) + r) == curr:
            break
        else:
            c+=1
    print(c)