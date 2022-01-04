# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, k = map(int, input().split())
    if (n%2!=0 and k>(n//2)+1) or n%2==0 and k>(n//2):
        print(-1)        
    else:
        cc = 0
        cline = 0
        while k>0:
            zz = ["."]*n
            if cline%2==0:
                zz[cc]="R"
                k-=1
                cc+=2
            print("".join(zz))
            cline+=1
        if cline<n:
            for i in range(abs(cline-n)):
                print("."*n)