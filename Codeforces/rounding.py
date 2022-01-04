# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n=int(input())
z=n
st1=0
st2=0
while n%10!=0:
    st1+=1
    n+=1
while z%10!=0:
    st2+=1
    z-=1
    
if st1<=st2:
    print(n)
else:
    print(z)