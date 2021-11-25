# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n = int(input())
s = input()
zz = 0
mi = 0-s.count('L')
max = s.count("R")
for i in range(mi, max+1):
    zz+=1
print(zz)