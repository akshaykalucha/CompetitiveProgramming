n = list(map(int, input().split()))
bb = 0

for el in set(n):
    if n.count(el) > 1:
        bb+=(n.count(el)-1)
print(bb)