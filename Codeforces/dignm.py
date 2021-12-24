# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n = int(input())
if n<=9:
    print(1)
    print(n)
else:
    for i in range(9,0, -1):
        if n%i==0:
            print(n//i)
            print(f"{i} "*(n//i))
            break