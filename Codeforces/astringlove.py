# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

s = list(input())
ac = s.count('a')
rc = len(s)-ac
if ac>rc:
    print(len(s))
else:
    rc = ac-1
    print(ac+rc)
