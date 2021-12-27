# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')
vov = "aeiou"
digs = "0123456789"

ll = list(input())
vc = 0
cc = 0
odd=0
for i in range(len(ll)):
    if ll[i] in vov:
        vc+=1
    elif ll[i] not in vov and ll[i] not in digs:
        cc+=1
    elif ll[i] in digs and int(ll[i])%2!=0:
        odd+=1
print(vc+odd)