# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    c1 = c2 = n//3
    if n%3 == 1: c1 += 1
    elif n%3 == 2: c2 += 1
    print(f'{c1} {c2}')