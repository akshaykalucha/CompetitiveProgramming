n = int(input())
ll = list(map(int, input().split()))

if len(ll) == 1:
    print(0)
else:
    cc = 0
    curmin = None
    currmax = None
    for i in range(len(ll)):
        if i==0:
            currmax = ll[i]
            curmin = ll[i]
        else:
            if ll[i] > currmax:
                cc+=1
                currmax=ll[i]
            if ll[i] < curmin:
                curmin = ll[i]
                cc+=1
    print(cc)
            