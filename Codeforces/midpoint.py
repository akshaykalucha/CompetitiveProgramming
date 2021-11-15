n = list(map(int, input().split()))
n.sort()

print((abs(n[0] - n[1])) + (abs(n[2]-n[1])))