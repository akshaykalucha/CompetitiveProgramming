for _ in range(int(input())):
    n = int(input())
    ll = [x for x in str(n)]
    ans = []
    for i in range(len(ll)):
        if ll[i]!="0":
            k = ll[i]+"0"*(len(ll)-(i+1))
            ans.append(k)
    print(len(ans))
    print(*ans)