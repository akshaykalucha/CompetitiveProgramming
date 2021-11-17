# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')


n, k, l, c, d, p, nl, np = map(int, input().split())

drink = (k*l)
pc = c*d
salt = p//np

print(min((drink)//nl,pc,salt)//n)