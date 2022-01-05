# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

alphs = [chr(i) for i in range(97,123)]

n, k = map(int, input().split())

ss = ""
for i in range(k):
    ss+=alphs[i]
i = 1
cc=0
while i<=n-k:
    if cc>len(ss):
        cc=0
    ss+=ss[cc]
    cc+=1
    i+=1

print(ss)