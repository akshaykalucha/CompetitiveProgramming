# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, t = map(int, input().split())
    s = input()
    for i in range(min(n,t)):
        s=s.replace('101', '121')
        s=s.replace('101', '121')
        s=s.replace('10', '11')
        s=s.replace('01', '11')
        
        s=s.replace('2', '0')
    print(''.join(s))