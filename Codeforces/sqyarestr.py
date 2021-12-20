# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    ss = input()
    n = len(ss)
    if n%2!=0:
        print("NO")
    else:
        if ss[:n//2] == ss[(n//2):]:
            print("YES")
        else:
            print("NO")