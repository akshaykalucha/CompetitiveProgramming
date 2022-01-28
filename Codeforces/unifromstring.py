# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, k = map(int, input().split())
    ss = ""
    oo = 97
    for i in range(k):
        ss+=chr(oo)
        if oo==122:
            
            oo=1
        else:
            oo+=1
    if n-k>0:
        cc=0
        for i in range(n-k):
            ss+=ss[cc]
            if cc==k-1:
                cc=0
            else:
                cc+=1
    print(ss)