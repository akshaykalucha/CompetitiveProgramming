# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


ranklist = []
for i in range(int(input())):
    ll = list(map(int, input().split()))
    rr = (i+1, sum(ll))
    ranklist.append(rr)
ranklist.sort(key=lambda x:x[1], reverse=True)
for i in range(len(ranklist)):
    if ranklist[i][0]==1:
        print(i+1)
        break