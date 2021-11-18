# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')
n = []
for i in range(5):
    mat = list(map(int, input().split()))
    n.append(mat)

ind = 1
pos = 1
for i in range(len(n)):
    if 1 in n[i]:
        ind = i+1
        pos = n[i].index(1)+1

i = 0
j = 0
if ind > 3:
    i+= ind-3
if ind < 3:
    i+=3-ind
    
if pos > 3:
    j+= pos-3
if pos < 3:
    j+=3-pos
print(i+j)