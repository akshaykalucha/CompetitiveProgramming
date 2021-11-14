n = int(input())
c = 0

while n > 0:
    if n >= 100:
        rem = n%100
        if rem == 0:
            c+=n//100
            break
        else:
            minus = n - rem
            remove = (n-rem)//100
            c+=remove
            n-=minus
    elif n >= 20:
        rem = n%20
        if rem == 0:
            c+=n//20
            break
        else:
            minus = n - rem
            remove = (n-rem)//20
            c+=remove
            n-=minus
    elif n >= 10:
        rem = n%10
        if rem == 0:
            c+=n//10
            break
        else:
            minus = n - rem
            remove = (n-rem)//10
            c+=remove
            n-=minus
    elif n >= 5:
        rem = n%5
        if rem == 0:
            c+=n//5
            break
        else:
            minus = n - rem
            remove = (n-rem)//5
            c+=remove
            n-=minus
    else:
        n-=1
        c+=1
print(c)