import sys
sys.stdout = open('Codeforces/output.txt', 'w')
sys.stdin = open('Codeforces/input.txt', 'r')

cubes = int(input())
i = 1
while cubes > 0:
    cursum = sum(range(1,i+1))
    if cursum > cubes:
        break
    cubes-=cursum
    i+=1
print(i-1)