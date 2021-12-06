# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for _ in range(int(input())):
    k = int(input())
    wat = 100-k
    gg = gcd(k, wat)
    k//=gg
    wat//=gg
    print(k+wat)