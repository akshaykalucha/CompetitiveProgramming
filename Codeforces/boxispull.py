# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    if x1==x2:
        print(abs(y2-y1))
    elif y1==y2:
        print(abs(x2-x1))
    else:
        if abs(y2-y1)==abs(x2-x1)==1:
            print(4)
        else:
            print((abs(x2-x1)+abs(y2-y1)+2))