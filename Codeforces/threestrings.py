# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    a = list(input())
    b = list(input())
    c = list(input())
    flag = True
    for i in range(len(c)):
        if c[i]==a[i] or c[i]==b[i]:
            continue
        else:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
        