import sys
sys.stdout = open('Codeforces/output.txt', 'w')
sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    weights = [2**i for i in range(1,n)]
    mw = (2**n)+(sum(weights[:(n//2)-1]))
    print(abs(mw-sum(weights[(n//2)-1:])))