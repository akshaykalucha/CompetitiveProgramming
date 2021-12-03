# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    a,b,k = map(int, input().split())
    pos = 0
    if k%2!=0:
        odds = ((k-1)//2)*b
        evens = ((k+1)//2)*a
        pos-= odds
        pos+= evens
    else:
        odds = (k//2)*b
        evens = (k//2)*a
        pos-= odds
        pos+= evens
    print(pos)