# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    s = int(input())
    start = [1]
    c = 1
    while True:
        if sum(start) >= s:
            break
        start.append(start[-1]+2)
        c+=1
    print(c)