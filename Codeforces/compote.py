# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')



a = int(input())
b = int(input())
c = int(input())
compote = 0
while True:
    if a<1:
        break
    if b<2:
        break
    if c<4:
        break
    a-=1
    compote+=1
    b-=2
    compote+=2
    c-=4
    compote+=4
print(compote)
    