n = int(input())
ll = list(map(int, input().split()))
currfree = 0
currcrime = 0

for i in range(len(ll)):
    if ll[i] == -1:
        if currfree > 0:
            currfree -= 1
        else:
            currcrime += 1
    else:
        currfree += ll[i]
print(currcrime)