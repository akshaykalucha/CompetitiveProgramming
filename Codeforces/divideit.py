# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    count2 = 0
    count3 = 0
    count5 = 0
    while n%2==0:
        n//=2
        count2+=1
    while n%3==0:
        n//=3
        count3+=1
    while n%5==0:
        n//=5
        count5+=1
    if n!=1:
        print(-1)
    else:
        print(count2+(count3*2)+(count5*3))