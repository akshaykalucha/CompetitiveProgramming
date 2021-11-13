k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

if 1 in [k,l,m,n]:
    print(d)
else:

    hit = []

    for i in range(1, d+1):
        if i >=k and i%k==0 and i not in hit:
            hit.append(i)
        elif i >=l and i%l==0 and i not in hit:
            hit.append(l)
        elif i >=m and i%m==0 and i not in hit:
            hit.append(m)
        elif i >=n and i%n==0 and i not in hit:
            hit.append(n)
    print(len(hit))