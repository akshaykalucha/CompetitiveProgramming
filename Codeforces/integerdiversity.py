# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    zz = set(ll)
    count = 0
    for el in zz:
        if ll.count(el)>=2 and el!=0 and -el not in ll:
            count+=2
        else:
            count+=1
    print(count)