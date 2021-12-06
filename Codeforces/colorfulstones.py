# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


stones = list(input())
c = list(input())
point = 0
for i in range(len(c)):
    if c[i]==stones[point]:
        point+=1
print(point+1)