# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

y,bl,r = map(int, input().split())
tot = 0
a = 0
b = 1
c = 2
while a<=y and b<=bl and c<=r:
    a+=1
    b+=1
    c+=1
print((a+b+c)-3)