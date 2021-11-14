n = int(input())
ll = list(map(int, input().split()))
minin = len(ll) - 1 - ll[::-1].index(min(ll))
maxin = ll.index(max(ll))

if minin < maxin:
    print(maxin + (len(ll) - (minin+2)))
else:
    print(maxin+(len(ll)-(minin+1)))