# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(input())
    if '8' in ll:
        if n-ll.index('8')>=11:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")