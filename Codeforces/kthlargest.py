n, q = map(int, input().split())
a = [int(i) for i in input().split()]
k = a.count(1)
for wq in range(q):
	t, x = map(int, input().split())
	if t == 1:
		x -= 1
		if a[x] == 1:
			k -= 1
		else:
			k += 1
		a[x] = 1 - a[x]
	else:
		print(int(x <= k))