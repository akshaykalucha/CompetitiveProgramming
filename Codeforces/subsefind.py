# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    a, b = map(int, input().split())
    ll = set(list(map(int, input().split())))
    mm = set(list(map(int, input().split())))
    flag = True
    zz = 0
    for el in ll:
        if el in mm:
            flag = False
            zz = el
            break
    if flag:
        print("NO")
    else:
        print("YES")
        print(1, zz)