# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    l, r = map(int, input().split())
    if abs(r-l)>=r//2:
        if r%2==0:
            print((r//2)-1)
        else:
            print(r//2)
    else:
        print(r%l)