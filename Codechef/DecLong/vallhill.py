import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n,m = map(int, input().split())
    if n==m:
        print((n*2)+2)
        print("01"*(n+1))
    elif m>n and m-n==1:
        print((m*2)+1)
        print("10"*m + "1")
    elif n>m and n-m==1:
        print((n*2)+1)
        print("0"+("10"*n))
    elif n>m and n-m > 1:
        print((2*(m+1))+1+(3*(n-(m+1))))
        print("0"+("10"*(m+1)) + "010"*(n-(m+1)))
    elif m>n and m-n>1:
        print(1+((n+1)*2)+(3*(m-(n+1))))
        print("1"+("01")*(n+1)+("101"*(m-(n+1))))