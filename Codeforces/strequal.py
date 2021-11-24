# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    zz = ""
    flag = True
    n = int(input())
    for _ in range(n):
        zz+=input()
    srt = set(zz)
    for el in srt:
        if zz.count(el)%n != 0:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")