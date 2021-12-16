# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

x,y,z = map(int, input().split())
a,b,c = map(int, input().split())
flag = True
if a>=x:
    a-=x
    if (a+b)>=y:
        rem = (a+b)-y
        if rem+c>=z:
            flag = False
            print("YES")
if flag:
    print("NO")