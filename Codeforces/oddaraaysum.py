for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    flag = False
    if sum(ll)%2!=0:
        flag = True
    else:
        for i in range(len(ll)-1):
            if ll[i]%2==0 and ll[i+1]%2!=0:
                flag = True
                break
            elif ll[i]%2!=0 and ll[i+1]%2==0:
                flag = True
                break
    if flag:
        print("YES")
    else:
        print("NO")