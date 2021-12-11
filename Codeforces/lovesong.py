# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

alph = [chr(i) for i in range(97,123)]
n,q = map(int, input().split())
s = list(input())

des = []
for i in range(len(s)):
    if i == 0:
        des.append(alph.index(s[i])+1)
    else:
        z = alph.index(s[i])+1
        des.append(des[-1]+z)
for i in range(q):
    l,r=map(int, input().split())
    k = 0
    if l==1:
        print(des[r-1])
    else:
        print(des[r-1]-des[l-2])