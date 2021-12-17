# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')
t=int(input())
for i in range(t-1):
  n,x=[int(x) for x in input().split()]
  a=[int(x) for x in input().split()]
  b=[int(x) for x in input().split()]
  s=input()
  a.sort()
  b.sort(reverse=True)
  check=1
  for i in range(n):
    if a[i]+b[i]>x:
      check=0
      break
  if check==1:
    print('Yes')
  else:
    print('No')

n,x=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
check=1
a.sort()
b.sort(reverse=True)
for i in range(n):
  if a[i]+b[i]>x:
    check=0
    break
if check==1:
  print('Yes')
else:
  print('No')