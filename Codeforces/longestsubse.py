# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

alphs = [chr(i) for i in range(65,91)]
n, k = map(int, input().split())
ll = list(input())
z = [0]*k
for i in range(len(ll)):
    z[alphs.index(ll[i])]+=1
if min(z)==0:
    print(0)
else:
    
    print(min(z)*k)
    
    
# freq = {i:ll.count(i) for i in ll}
# for j in range(len(alphs)):
#     if alphs[j] in freq.keys():
#         continue
#     else:
#         freq[alphs[j]]=0
# f=True
# cmin = 9999999999999
# for i in range(k):
#     if freq[alphs[i]]==0:
#         print(0)
#         f=False
#         break
#     else:
#         cmin=min(cmin,freq[alphs[i]])
# if f:
#     print(cmin*k)