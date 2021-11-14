n, m = map(int, input().split())
curr = 0
for i in range(1, n+1):
    if i%2!=0:
        print("#"*m)
    else:
        if curr == 0:
            print("."*(m-1)+"#")
            curr = 1
        else:
            print("#"+"."*(m-1))
            curr = 0
