# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n = int(input())
s = list(input())
st = ""
times=1
i = 0
while i<n:
    currchar = s[i]
    st = st+s[i]
    times+=1
    i+=(times-1)
print(st)
    