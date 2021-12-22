# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    f, s, t = map(int, input().split())
    a,b,c = f,s,t
    st1 = 0
    st2 = 0
    while f>=1 and s>=2:
        f-=1
        s-=2
        st1+=3
    while s>=1 and t>=2:
        s-=1
        t-=2
        st1+=3
    while b>=1 and c>=2:
        b-=1
        c-=2
        st2+=3
    while a>=1 and b>=2:
        a-=1
        b-=2
        st2+=3
    print(max(st1,st2))