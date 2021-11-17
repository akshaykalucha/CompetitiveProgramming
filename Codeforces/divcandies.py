# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    cand = list(map(int, input().split()))
    if n == 1:
        print("NO")
    else:
        if n%2!=0:
            if sum(cand)%2==0:
                if (cand.count(2)*2)%2==0 and (cand.count(1))%2==0 and (cand.count(1))>1:
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")
        else:
            if sum(cand)%2!=0:
                print("NO")
            else:
                print("YES")