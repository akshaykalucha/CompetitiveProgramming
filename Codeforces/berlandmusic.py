# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    rr = list(map(int, input().split()))
    ss = input()
    kk = set(ss)
    if len(kk)==1:
        print(*rr)
    else:
        z1 = []
        o1 = []
        ones = ss.count("1")
        zeros = n-ones
        z2=list(range(1,zeros+1))
        o2=list(range(zeros+1, n+1))
        for i in range(n):
            if ss[i]=="1":
                o1.append(rr[i])
            else:
                z1.append(rr[i])
        o1.sort()
        z1.sort()
        onemap={}
        zeromap={}
        for i in range(len(o1)):
            onemap[o1[i]]=o2[i]
        for i in range(len(z1)):
            zeromap[z1[i]]=z2[i]
        ans=[]
        for i in range(n):
            if ss[i]=="0":
                ans.append(zeromap[rr[i]])
            else:
                ans.append(onemap[rr[i]])
        print(*ans)