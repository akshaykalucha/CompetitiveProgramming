# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    ll = [x for x in input()]
    ss = ""
    for i in range(n):
        arr = ll[i:n+i]
        ss+=arr[i]
    print(ss)