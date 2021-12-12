# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n = int(input())
ll = list(map(int, input().split()))
print(ll.count(1))
ll=ll[::-1]
i = 0
ss = [ll[0]]
while i < n-1:
    if ll[i]==1:
        ss.append(ll[i+1])
    i+=1
print(*ss[::-1])