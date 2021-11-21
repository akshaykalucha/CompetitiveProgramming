# import sys
# sys.stdin = open('Codeforces/input.txt', 'r')
# sys.stdout = open('Codeforces/output.txt', 'w')

n = int(input())
curr = input()
curr = [int(el) for el in curr]
fin = input()
fin = [int(el) for el in fin]
s = 0
for i in range(n):
    dist1 = abs(curr[i]-fin[i])
    dist2 = abs(abs(curr[i])+abs(9-fin[i])+1)
    dist3 = abs(abs(curr[i]-9)+fin[i]+1)
    s+=min(dist1, dist2, dist3)
print(s)