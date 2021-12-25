import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    l, r = map(int, input().split())
    nd = l
    for i in range(l+1,r+1):
        nd&=i
    print(nd)