# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n = int(input())
ll = list(map(int, input().split()))
for i in range(len(ll)):
    if ll[i]%2==0:
        ll[i]-=1
        
print(*ll)