for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    maxx = 0
    for i in range(n-k+1):
        if maxx < sum(arr[i:k+i]):
            maxx = sum(arr[i:k+i])
    print(maxx) 