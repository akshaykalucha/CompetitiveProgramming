# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = ""
i=1
while len(ll)<n:
    ll+=str(i)
    i+=1
print(ll[n-1])
# print(ll)