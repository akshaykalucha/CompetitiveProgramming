# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    ll = list(input())
    st = []
    cc = 0
    tot = 0
    for i in range(len(ll)):
        if ll[i] == '1':
            if len(st)!=0:
                tot += cc
                cc = 0
            else:
                cc = 0
                st.append('1')
        if ll[i]=='0':
            cc+=1
    print(tot)