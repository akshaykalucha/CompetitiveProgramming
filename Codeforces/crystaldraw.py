# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll=[]
st=1
if n==1:
    print("D")
else:
    for i in range((n+1)//2):
        spaces = "*"*((n-st)//2)
        ss = spaces+"D"*st+spaces
        ll.append(ss)
        st+=2
    for el in ll:
        print(el)
    for j in range(len(ll)-2,-1,-1):
        print(ll[j])