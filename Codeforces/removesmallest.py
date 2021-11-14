for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    ll.sort()

    if len(ll)==1:
        print("YES")
    else:
        flag = True
        for i in range(len(ll)-1):
            if abs(ll[i]-ll[i+1])>1:
                flag = False
                break
        if flag:
            print("YES")
        else:
            print("NO")