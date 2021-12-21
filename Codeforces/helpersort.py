t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    i = 0
    while a != b:
        for j in range(i % 2, n - 1, 2):
            if a[j] > a[j+1]:
                a[j], a[j+1]=a[j+1], a[j]
                j += 1
        i += 1
    print(i)