# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = list(map(int, input().split()))
prev = 0
ll.sort()
while len(ll)!=0:
    if ll[-1]!=ll[-2]:
        prev+=abs(ll[-1]-ll[-2])
    ll.pop()
    ll.pop()
print(prev)