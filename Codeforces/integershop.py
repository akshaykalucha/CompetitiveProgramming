# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')
for _ in range(int(input())):
     
    
    n=int(input())
    low,high,cost=[int(k) for k in input().split()]
    lowcost=cost
    highcost=cost
    print(cost)
    for j in range(n-1):
        l,r,c=[int(k) for k in input().split()]
        if low>l and high<r:
            lowcost=c
            highcost=c
            cost=c
            low=l
            high=r
        elif low>l:
            lowcost=c
            low=l
            if r==high:
                cost=c
                if highcost>c:
                    highcost=c
            else:
                cost=lowcost+highcost
        elif high<r:
            highcost=c
            high=r
            if l==low:
                cost=c
                if lowcost>c:
                    lowcost=c
            else:
                cost=lowcost+highcost
        elif low==l and high==r:
            if cost>c:
                cost=c
                if highcost>c:
                    highcost=c
                if lowcost>c:
                    lowcost=c
        elif low==l:
            if lowcost>c:
                lowcost=c
            if lowcost+highcost<cost:
                cost=lowcost+highcost
        elif high==r:
            if highcost>c:
                highcost=c
            if lowcost+highcost<cost:
                cost=lowcost+highcost
        print(cost)