# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

a,b,c = map(int, input().split())

st = 0
maxside = max(a,b,c)
min1 = min(a,b,c)
if min1 == a:
    min2 = min(b,c)
elif min1 == b:
    min2 = min(a,c)
elif min1 == c:
    min2 = min(a,b)

if min1+min2 <= maxside:
    st = maxside - (min1+min2)+1
print(st)