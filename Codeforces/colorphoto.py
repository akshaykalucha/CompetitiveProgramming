# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

n, m = map(int, input().split())
flag = True
for i in range(n):
    row = list(map(str, input().split()))
    if "C" in row or "M" in row or "Y" in row:
        flag = False
if flag == True:
    print("#Black&White")
else:
    print("#Color")