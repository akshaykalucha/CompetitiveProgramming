# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')
a = int(input())
 
h = {"purple":"Power", "green":"Time", "blue":"Space", "orange":"Soul",
     "red":"Reality", "yellow":"Mind"}
l = []
for x in range(a):
    z = input()
    l.append(z)
 
print(6-a)
for i in h:
    x = i
    y = h[i]
    if x not in l:
        print(y)