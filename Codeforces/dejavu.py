# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    s = list(input())
    if len(set(s))==1 and s[0]=='a':
        print("NO")
    else:
        print('YES')
        if s[-1]=='a' and s[0]!='a':
            s.append('a')
        elif s[0]=='a'and s[-1]!='a':
            s=['a']+s
        elif s[0]=='a' and s[-1]=='a':
            front=0
            back=0
            for i in range((len(s))):
                if s[i]!='a':
                    front=i
                    break
            for i in range(len(s)-1,0,-1):
                if s[i]!='a':
                    back=len(s)-i-1
                    break
            if front<=back:
                s.append('a')
            elif front>back:
                s=['a']+s
        else:
            s=['a']+s
        print("".join(s))