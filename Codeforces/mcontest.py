# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n,k=map(int, input().split())
ll = list(map(int, input().split()))
n = 0
while len(ll)>0:
    if ll[0]<=k:
        n+=1
        ll.pop(0)
    elif ll[-1]<=k:
        n+=1
        ll.pop()
    elif ll[-1]> k and ll[0]>k:
        break      
print(n)  