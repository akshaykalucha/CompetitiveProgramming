k, n, w = map(int, input().split())
price = 0
for i in range(w):
    price+=((i+1)*k)
if price-n>0:
    print(price-n)
else:
    print(0)