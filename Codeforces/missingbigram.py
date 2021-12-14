# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    s = list(map(str, input().split(" ")))
    mys = ""
    check = False
    for i in range(len(s)):
        if i == 0:
            mys+=s[i]
        else:
            if s[i][0]==s[i-1][1]:
                mys+=s[i][1]
            else:
                mys+=s[i]
                check=True
    if check:
        print(mys)
    else:
        print(mys+s[-1][1])