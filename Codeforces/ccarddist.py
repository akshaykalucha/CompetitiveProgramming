# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n = int(input())
ll = list(map(int, input().split()))
ss = max(ll)+min(ll)
done = []
while len(done)<n:
    for i in range(n):
        for j in range(i+1, n):
            if ll[i]+ll[j]==ss and j not in done and i not in done:
                done.append(j)
                done.append(i)
                print(i+1,j+1)
                break