# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
flag = True
ll = []
for i in range(n):
    zz = input()
    kk = zz.split("|")
    for j in range(len(kk)):
        if kk[j] == "OO" and flag==True:
            kk[j] = "++"
            flag = False
    ll.append(kk)
if flag:
    print("NO")
else:
    print("YES")
    for i in range(len(ll)):
        print(f"{ll[i][0]}|{ll[i][1]}")