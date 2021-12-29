# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(input())
    ss = 0
    for i in range(len(ll)-1):
        if ll[i+1]<ll[i]:
            ss=i+1
        else:
            break
    mystr = "".join(ll[:ss+1])
    print(mystr+mystr[::-1])