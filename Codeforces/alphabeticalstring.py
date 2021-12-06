# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


alph = list(chr(i) for i in range(97,123))

for _ in range(int(input())):
    s = list(input())
    flag = True
    z = set(s)
    if max(s)>alph[len(s)-1] or max(s)<alph[len(s)-1] or len(z)!=len(s):
        flag=False
    else:
        aind = s.index('a')
        st = "a"
        for i in range(1,len(s)):
            curralph = alph[i]
            kk = s.index(curralph)
            if kk<aind:
                st = curralph+st
            else:
                st=st+curralph
        giv = "".join(s)
        if st!=giv:
            flag=False
    if flag:
        print("YES")
    else:
        print("NO")