# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    el = 0
    flag = True
    while flag:
        if n&(n-1)==0:
            el = n-1
            flag = False
        else:
            n = n&(n-1)
    print(el)