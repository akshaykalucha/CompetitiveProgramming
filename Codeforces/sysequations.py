# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n, m = map(int, input().split())
p = 0
for i in range((n+1)//2 + 1):
    a = i
    for j in range((m+1)//2 + 1):
        b = j
        if(a**2+b)==n and (a+b**2)==m:
            p+=1
print(p)