# import sys
# sys.stdin = open('Codeforces/input.txt', 'r')
# sys.stdout = open('Codeforces/output.txt', 'w')

for _ in range(int(input())):
    n, d = map(int, input().split())
    ll = list(map(int, input().split()))
    ll.sort()
    ss = ll[0]+ll[1]
    flag = True
    for i in range(len(ll)):
        if ll[i]>d:
            if ss>d:
                flag=False
                break
    if flag:
        print("YES")
    else:
        print("NO")