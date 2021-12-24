# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

def fib(n, memo):
    if n == 0 or n == 1:
        return n
    if memo[n]!=0:
        return memo[n]
    fibn = fib(n-1, memo)+fib(n-2, memo)
    memo[n]=fibn
    return fibn        

n = int(input())
memo = [0]*(n+11)
fib(n+10, memo)
for i in range(1, n+1):
    if i in memo:
        print("O",end="")
    else:
        print("o", end="")