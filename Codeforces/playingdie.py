# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

a,b = map(int, input().split())
wa=0
wb=0
d=0

for i in range(1,7):
    if abs(i-a)>abs(i-b):
        wa+=1
    elif abs(i-a)<abs(i-b):
        wb+=1
    else:
        d+=1
print(wb,d,wa)    