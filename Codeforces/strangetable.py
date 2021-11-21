import sys
sys.stdin = open('Codeforces/input.txt', 'r')
sys.stdout = open('Codeforces/output.txt', 'w')

import math
t=int(input())
 
for x in range(t):
    n,m,x = [int(x) for x in input().split()]
    
    r=x%n
    
    if(r==0):
        
        c=math.floor(x/n)
        r=n
    else:
        c=math.floor(x/n) + 1
    
    print(m*(r-1)+c)