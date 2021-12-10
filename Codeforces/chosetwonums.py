# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
la = list(map(int, input().split()))
m = int(input())
lb = list(map(int, input().split()))
la.sort()
lb.sort()
print(la[-1],lb[-1])