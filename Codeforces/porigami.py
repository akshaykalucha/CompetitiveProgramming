# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n, k = map(int, input().split())
if (2*n)%k==0:
    red = (2*n)//k
else:
    red = ((2*n)//k)+1
if (5*n)%k==0:
    green = (5*n)//k
else:
    green = ((5*n)//k)+1
if (8*n)%k==0:
    blue = (8*n)//k
else:
    blue = ((8*n)//k)+1
print(red+green+blue)