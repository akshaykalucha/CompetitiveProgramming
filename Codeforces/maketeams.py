n = int(input())
ll = list(map(int, input().split()))

if 1 not in ll or 2 not in ll or 3 not in ll:
    print(0)
else:
    players = min(ll.count(1), ll.count(2), ll.count(3))
    print(players)
    pr = ll.index(1)
    ma = ll.index(2)
    ped = ll.index(3)
    for i in range(players):
        if i == 0:
            print(pr+1, ma+1, ped+1)
        else:
            Cpr = ll[pr+1:].index(1)
            Cma = ll[ma+1:].index(2)
            Cped = ll[ped+1:].index(3)
            pr += Cpr+1
            ma += Cma + 1
            ped += Cped+1
            print(pr+1, ma+1, ped+1)