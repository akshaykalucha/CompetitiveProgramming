# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

string = input()
res = 0
for i in range(len(string)):
    if string[i] == 'A':
        res += (string[:i].count('Q') * string[i:].count('Q'))
print(res)