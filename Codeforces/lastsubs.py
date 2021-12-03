# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

def solve(s):
    if (s[0:3]=="202" and s[-1]=="0") or (s[0:4]=="2020") or (s[0:2]=="20" and s[-2:]=="20") or (s[0]=="2" and s[-3:]=="020") or (s[-4:]=="2020") or s[:3]=="2020":
        return True
    else:
        return False

for _ in range(int(input())):
    n = int(input())
    s = input()
    if solve(s):
        print("YES")
    else:
        print("NO")