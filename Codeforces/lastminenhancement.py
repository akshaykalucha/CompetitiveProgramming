# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    st = set()
    for i in range(len(ll)):
        if ll[i] not in st:
            st.add(ll[i])
        else:
            if ll[i]+1 not in st:
                st.add(ll[i]+1)
    print(len(st))