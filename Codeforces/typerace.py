# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

s,v1,v2,t1,t2 = map(int, input().split())
firsttime = t1*2+(s*v1)
secondtime = t2*2+(s*v2)
if firsttime<secondtime:
    print("First")
elif secondtime<firsttime:
    print("Second")
else:
    print("Friendship")