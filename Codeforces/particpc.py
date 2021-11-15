n, k = map(int, input().split())
ll = list(map(int, input().split()))
lim = 5
ll.sort()
ll = [x+k for x in ll]
c = 0
i = 0
while i<=len(ll)-3:
    if ll[i]<=lim and ll[i+1]<=lim and ll[i+2]<=lim:
        c+=1
        i+=3
    else:
        break
print(c)