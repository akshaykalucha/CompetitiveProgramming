# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = []
    if n%2==0:
        for i in range(1,n+1):
            if i%2!=0:
                ll.append(i+1)
            else:
                ll.append(i-1)
    else:
        for i in range(1,n+1):
            if i == 1:
                ll.append(3)
            elif i == 2:
                ll.append(1)
            else:
                if i%2!=0:
                    ll.append(i-1)
                else:
                    ll.append(i+1)
    print(*ll)