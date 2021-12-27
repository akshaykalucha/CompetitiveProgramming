# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    ll = list(map(int, input().split()))
    ll.sort()
    if ll[0]==ll[1]==ll[2] and ll[2]%2==0:
        print("YES")
    elif ll[0]==ll[1]==ll[2] and ll[2]%2!=0:
        print("NO")
    elif ll[0]==ll[1]:
        if ll[2]%2==0:
            print("YES")
        else:
            print("NO")
    elif ll[1]==ll[2]:
        if ll[0]%2==0:
            print("YES")
        else:
            print("NO")
    elif ll[0]!=ll[1]!=ll[2]:
        if ll[0]+ll[1]==ll[2]:
            print("YES")
        else:
            print("NO")
