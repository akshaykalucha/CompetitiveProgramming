# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n, k = map(int, input().split())
coutn = 0
ll = list(map(int, input().split()))
for i in range(len(ll)):
    num = str(ll[i])
    totlucky = num.count('4')+num.count('7')
    if totlucky<=k:
        coutn+=1
print(coutn)