# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

d1, d2, d3 = map(int, input().split())

way1 = d1*2+d2*2
way2 = d1+d2+d3
way3 = d2*2 + d3*2
way4 = d1*2+d3*2
print(min(way1,way2,way3,way4))