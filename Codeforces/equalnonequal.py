# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    ll = list(input())
    f = True
    if len(ll)==2 and ll[0]=="E" and ll[1]=="N" or len(ll)==2 and ll[0]=="N" and ll[1]=="E":
        print("NO")
    else:
        if ll[-1]=="N":
            if ll.count("N")>=2:
                print("YES")
            else:
                print("NO")
        elif ll[-1]=="E":
            if ll.count("N")>=2 or ll.count("N")==0:
                print("YES")
            else:
                print("NO")