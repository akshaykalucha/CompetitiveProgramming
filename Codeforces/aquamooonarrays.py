# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
#     n = int(input())
#     aa = list(map(int, input().split()))
#     bb = list(map(int, input().split()))
#     f = True
#     if sum(aa)!=sum(bb):
#         f = False
#     add = []
#     subs = []
#     if f:
#         for i in range(len(aa)):
#             if aa[i]!=bb[i]:
#                 if aa[i]>bb[i]:
#                     fin = abs(bb[i]-aa[i])
#                     zz = [i+1]*fin
#                     subs = subs+zz
#                 elif aa[i]<bb[i]:
#                     fin = abs(bb[i]-aa[i])
#                     zz = [i+1]*fin
#                     add = add+zz
#         if len(subs)==len(add)==0:
#             print(0)
#         else:
#             print(len(subs))
#             for i in range(len(subs)):
#                 print(subs[i], add[i])
#     else:
#         print(-1)

    a,b = map(int, input().split())
    print(a+b)