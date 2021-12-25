# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n, m = map(int, input().split())
i = 1
while m>0:
    cc = i%n
    if cc==0:
        cc=n
    if m-cc<0:
        break
    m-=cc
    i+=1
print(m)