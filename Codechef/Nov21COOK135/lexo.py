import sys
sys.stdin = open("Codeforces/input.txt", 'r')
sys.stdout = open("Codeforces/output.txt", 'w')

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    z = 0
    end = b[n-1]>a[n-1]
    if end:
        z+=1
    i = n-2
    while i>=0:
        if b[i]>a[i]:
            end = True
            z+=1
        elif b[i]<a[i]:
            end=False
        else:
            if end:
                z+=1
        i-=1
    print(z)