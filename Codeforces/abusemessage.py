# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    ll = list(input())
    braks = 0
    for i in range(len(ll)-1,-1,-1):
        if ll[i]==")":
            braks+=1
        else:
            break
    if braks > len(ll)-braks:
        print("Yes")
    else:
        print("No")