# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

# def intsum(x):
#     s1 = 0
#     s2 = 0
#     for el in str(x):
#         s1+=int(el)
#     for el in str(x+1):
#         s2+=int(el)
#     if s2 > s1:
#         return True
#     return False

for i in range(int(input())):
    n = int(input())
    print((n + 1 ) // 10)