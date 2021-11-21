import sys
sys.stdin = open('Codeforces/input.txt', 'r')
sys.stdout = open('Codeforces/output.txt', 'w')
for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(n*2+i)
    print(*arr)