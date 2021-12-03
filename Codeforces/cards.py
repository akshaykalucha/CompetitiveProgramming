# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
s = input()
zes = s.count('z')
on = s.count('n')

for i in range(on):
    print(1, end=" ")
for i in range(zes):
    print(0, end=" ")