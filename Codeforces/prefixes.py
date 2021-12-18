# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = list(input())
ac = 0
bc = 0
op = 0
for i in range(len(ll)):
    if ll[i]=='a':
        ac+=1
    elif ll[i]=='b':
        bc+=1
    if (i+1)%2==0:
        if bc>ac:
            op+=1
            ll[i]='a'
            ac+=1
            bc-=1
        elif ac>bc:
            op+=1
            ll[i]='b'
            bc+=1
            ac-=1
print(op)
print("".join(ll))