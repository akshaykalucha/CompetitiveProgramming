import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
m = [0]*(n+1)
def fibmem(n, mem):
    if n == 0 or n == 1:
        return n
    if mem[n]!=0:
        return mem[n]
    ans = fibmem(n-1, m)+fibmem(n-2, m)
    mem[n]=ans
    return ans

print(fibmem(n, m))