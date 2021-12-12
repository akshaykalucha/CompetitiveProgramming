# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = list(map(int, input().split()))
print(len(set(ll)))
ll = ll[::-1]
seq = []
z = set(ll)
for el in z:
    seq.append(len(ll)-ll.index(el)-1)
seq.sort()
ll = ll[::-1]
for el in seq:
    print(ll[el], end=" ")