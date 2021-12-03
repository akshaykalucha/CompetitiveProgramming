# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    x, y = map(int, input().split())
    s = input()
    flag = False
    right = s.count('R')
    left = s.count("L")
    up = s.count("U")
    down = s.count("D")
    if x>=0 and y>=0 and right>=x and up>=y:
        flag = True
    elif x<=0 and y>=0 and left>=abs(x) and up>=y:
        flag = True
    elif x<=0 and y<=0 and left>=abs(x) and down>=abs(y):
        flag = True
    elif x>=0 and y<=0 and right>=x and down>=abs(y):
        flag = True
    if flag:
        print("YES")
    else:
        print("NO")