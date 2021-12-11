# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n,c=map(int, input().split())
ll=list(map(int, input().split()))
cc = 0
for i in range(len(ll)):
    if i == 0:
        cc+=1
    else:
        if ll[i]-ll[i-1]<=c:
            if cc==0:
                cc+=2
            else:
                cc+=1
        else:
            cc=0
if cc==0:
    print(1)
else:
    print(cc)