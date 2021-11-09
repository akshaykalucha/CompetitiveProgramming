# cook your dish here
for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    flag = False
    copy = []
    ss = set(ll)
    if ll.count(max(ll)) > 1:
        flag = True
    else:
        for el in ss:
            if ll.count(el) > 2:
                flag = True
                break
            elif ll.count(el) == 2:
                copy.append(el)
    if flag == True:
        print(-1)
    else:
        print(*(sorted(copy) + list(ss)[::-1]))