ll = list(map(int, input().split()))

ss = max(ll)
ll.pop(ll.index(ss))
ll = [ss-x for x in ll]
print(*ll)