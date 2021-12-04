# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

def freq(L):
    # z = set(L)
    # if len(z)==1 or len(z)==len(L):
    #     return 1
    d = {}
    for el in L:
        if el in d:
            d[el]+=1
        else:
            d[el]=1
    return d[max(d, key=d.get)]

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    freqq= freq(ll)
    if freqq ==  n or n==1:
        print(0)
    else:
        if freqq >=2:
            print(n-freqq+1)
        else:
            print(-1)