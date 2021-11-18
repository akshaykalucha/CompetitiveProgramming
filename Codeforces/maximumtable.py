# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

n = int(input())
mat = []
for i in range(n):
    if i == 0:
        mat.append([1]*n)
    else:
        mat.append([1]+[0]*(n-1))

for i in range(1, len(mat)):
    zz = mat[i]
    for j in range(1, len(zz)):
        zz[j] = zz[j-1]+mat[i-1][j]

print(mat[n-1][n-1])