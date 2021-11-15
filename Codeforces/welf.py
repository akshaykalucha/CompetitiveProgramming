n = int(input())
ll = list(map(int, input().split()))
sp = max(ll)
c = 0
for i in range(len(ll)):
    if ll[i]!=sp:
        c += abs(sp-ll[i])
print(c)