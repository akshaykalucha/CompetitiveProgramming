# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    s = list(input())
    if len(set(s))==1:
        print(-1, -1)
    else:
        flag = False
        for i in range(len(s)-1):
            if s[i]=='a' and s[i+1]=='b':
                print(i+1, i+2)
                break
            elif s[i]=='b' and s[i+1]=='a':
                print(i+1,i+2)
                break