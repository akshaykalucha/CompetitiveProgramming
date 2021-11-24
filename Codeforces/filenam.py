# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
s = input()
st = []
cc = 0
for i in range(len(s)):
    if s[i] != "x":
        st=[]
    else:
        if len(st)==2:
            cc+=1
        elif len(st)<2:
            st.append("x")
print(cc)