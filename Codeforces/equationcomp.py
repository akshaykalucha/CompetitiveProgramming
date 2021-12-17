# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True

n = int(input())

if n%2==0 and n!=2:
    print(n*2, n)
else:
    curr = n*2
    while True:
        if is_prime(curr) or is_prime(n) or n==2:
            curr+=1
            n+=1
        else:
            break
    print(curr, n)