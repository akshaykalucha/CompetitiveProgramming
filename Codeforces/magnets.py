# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

n = int(input())
l = []
c = 1
for i in range(n):
    x = int(input())
    l.append(x)
for i in range(len(l)):
    if i + 1 < n:
        if l[i] != l[i + 1]:
            c += 1
print(c)