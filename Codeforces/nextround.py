n,k=map(int, input().split())
ll=list(map(int, input().split()))
score = ll[k-1]
if max(ll) == 0:
    print(0)
else:
    c = 0
    for i in range(len(ll)):
        if score == 0:
            if ll[i] > score:
                c+= 1
        else:
            if ll[i] >= score:
                c+= 1
    print(c)