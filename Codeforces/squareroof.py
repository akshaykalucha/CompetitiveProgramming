# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    ll.sort(reverse=True)
    cln = 0
    cheight = 0
    for i in range(len(ll)):
        if ll[i]>cln:
            cln+=1
            ceight = ll[i]
        else:
            break
    print(cln)