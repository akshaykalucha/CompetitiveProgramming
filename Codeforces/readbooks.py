# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

chptrs = []

for _ in range(int(input())):
    chp = list(map(int, input().split()))
    chptrs.append(chp)
num = int(input())
for i in range(len(chptrs)):
    if num>=chptrs[i][0] and num <=chptrs[i][1]:
        print(len(chptrs)-(i))
        break