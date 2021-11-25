# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    if n%2==0:
        print(0)
    else:
        if int(str(n)[0])%2==0:
            print(1)
        else:
            odd = 0
            zz = str(n)
            for i in range(len(zz)):
                if int(zz[i])%2!=0:
                    odd+=1
            if len(zz)==odd:
                print(-1)
            else:
                print(2)