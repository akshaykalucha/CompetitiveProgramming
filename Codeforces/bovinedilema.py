# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

def dist(x1,x2,y1,y2):
    return ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

for _ in range(int(input())):
    n = int(input())
    p1 = [0,1]
    areas = set()
    ll = list(map(int, input().split()))
    height = 1
    for i in range(len(ll)-1):
        cc = ll[i]
        difflist = ll[i+1:]
        for j in range(len(difflist)):
            base = abs(difflist[j]-cc)
            area = 0.5*base*height
            areas.add(area)
    print(len(areas))