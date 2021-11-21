# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

from math import sqrt
 
def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
    return True
def nextPrime(N):
    if (N <= 1):
        return 2
    prime = N
    found = False
    while(not found):
        prime = prime + 1
        if(isPrime(prime) == True):
            found = True
    return prime
n, m = map(int, input().split())
if isPrime(n) and nextPrime(n)==m:
    print("YES")
else:
    print("NO")