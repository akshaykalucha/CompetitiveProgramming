# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    a, b = map(int, input().split())
    if a<2 and b<2:
        print(0)
    elif a==b and a+b>=4:
        print((a+b)//4)
    else:
        if a ==1 and b > 2 or a > 2 and b == 1:
            print(1)
        elif a == 2 and b > 6 or a > 6 and b == 2:
            print(2)
        else:
            if a > b*3:
                print(b)
            elif b > a*3:
                print(a)
            else:
                print((a+b)//4)