# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

a = int(input())
zz = list(int(x) for x in str(a))
while True:
    zz = list(int(x) for x in str(a))
    if sum(zz)%4==0:
        print(a)
        break
    else:
        a+=1