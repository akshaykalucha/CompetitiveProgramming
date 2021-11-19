# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

tableCard = input()
ll = list(map(str, input().split()))
suit = tableCard[1]
rank = tableCard[0]
flag = False
for i in range(len(ll)):
    if ll[i][0]==rank or ll[i][1]==suit:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")