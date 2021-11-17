# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n = input()
    print(((int(n[0]) - 1)*10) + sum([x for x in range(1,len(n)+1)]))
    