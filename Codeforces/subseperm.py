# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    s = list(input())
    z = s.copy()
    z.sort()
    c = 0
    for i in range(len(s)):
        if s[i]!=z[i]:
            c+=1
    print(c)