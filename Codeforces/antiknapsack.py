# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')



for _ in range(int(input())):
    n,k = map(int, input().split())
    
    ll = [i for i in range(k+1, n+1)]
    i = 1
    k-=1
    while k >= i:
        ll.append(k)
        k-=1
        i+=1
    if len(ll)==0:
        print(0)
    else:
        print(len(ll))
        print(*ll)