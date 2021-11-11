c = 0
for _ in range(int(input())):
    ll = list(map(int, input().split()))
    if ll.count(1)>=2:
        c += 1
print(c)