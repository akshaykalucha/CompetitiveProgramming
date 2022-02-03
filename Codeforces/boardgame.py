import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = list(map(int, input().split()))
ll.sort()
turn = True
while len(ll)>1:
    if turn:
        ll.pop()
        turn = False
    else:
        ll = ll[1:]
        turn = True
print(*ll)