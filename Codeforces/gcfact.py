import math
 
def gcdOfFactorial(m, n) :
    return math.factorial(min(m, n))
a, b = map(int, input().split())
print(gcdOfFactorial(a,b))