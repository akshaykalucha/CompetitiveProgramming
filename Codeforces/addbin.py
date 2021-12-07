# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


def read_int():
    return int(input())
 
 
t = read_int()
for case_num in range(t):
    n = read_int()
    b = input()
    a = []
    for i, c in enumerate(b):
        if i == 0:
            a.append('1')
        else:
            last = int(b[i - 1]) + int(a[i - 1])
            if last == 2:
                a.append('1' if c == '0' else '0')
            elif last == 1:
                a.append('1' if c == '1' else '0')
            else:
                a.append('1')
    print(''.join(a))

# for _ in range(int(input())):
#     n=int(input()); arr=input(); ans=str(int(arr[0])+1); a='1'
#     for i in range(1,n):
#         if 1+int(arr[i])==int(ans[-1]): ans+=str(int(arr[i])+0);a+='0'
#         else: ans+=str(int(arr[i])+1);a+='1'
#     print(a)  
    
# for _ in range(int(input())):
#     n = int(input())
#     a = input()
#     ans = ""
#     s = ""
#     for i in range(len(a)):
#         if i == 0:
#             if a[i]=="0":
#                 s+="1"
#                 ans+="1"
#             if a[i]=="1":
#                 s+="1"
#                 ans+="2"
#         else:
#             if a[i]=="0":
#                 if ans[-1]=="0":
#                     s+="1"
#                     ans+="1"
#                 elif ans[-1]=="1":
#                     s+="0"
#                     ans+="0"
#                 elif ans[-1]=="2":
#                     s+="1"
#                     ans+="1"
#             if a[i]=="1":
#                 if ans[-1]=="0":
#                     s+="1"
#                     ans+="2"
#                 elif ans[-1]=="1":
#                     s+="1"
#                     ans+="2"
#                 elif ans[-1]=="2":
#                     ans+="1"
#                     s+="0"
#     print(s)