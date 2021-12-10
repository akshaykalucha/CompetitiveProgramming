# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    x,y = map(int, input().split())
    zz = min(x,y)
    ans = zz*2
    rem = max(x,y)-min(x,y)
    if rem == 0:
        print(ans)
    else:
        ans+=1
        rem-=1
        ans+=(rem*2)
        print(ans)