# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n, m = map(int, input().split())
bb = [i for i in range(1,m+1)]
done = []
for i in range(n):
    ll = list(map(int, input().split()))
    but = ll[0]
    ll = ll[1:]
    for j in range(len(ll)):
        if ll[j] not in done:
            done.append(ll[j])
done.sort()
if done == bb:
    print("YES")
else:
    print("NO")