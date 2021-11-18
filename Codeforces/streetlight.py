q = int(input())
for z in range(q):
    str1 = input()
    n, m = (int(x) for x in str1.split())
    print(int((n * m + 1) / 2))