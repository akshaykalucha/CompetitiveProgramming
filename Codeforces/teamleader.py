# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

n = int(input())
cc = 0
i = n//2

for i in range(1, i+1):
    n-=1
    if n%i==0:
        cc+=1
    i+=1
print(cc)