# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    s = list(input())
    c = 0
    st = []
    for i in range(len(s)):
        if s[i]=="(":
            st.append("(")
        elif s[i]==")":
            if len(st)!=0:
                st.pop()
                c+=1
    st = []
    for i in range(len(s)):
        if s[i]=="[":
            st.append("[")
        elif s[i]=="]":
            if len(st)!=0:
                st.pop()
                c+=1  
    print(c)