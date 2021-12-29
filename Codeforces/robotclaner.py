# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for i in range(int(input())):
    line = input()
    rows, cols, x1, y1, x2, y2 = map(int, line.split(' '))
 
    if x2 >= x1:
        x_value = x2 - x1
    else:
        x_value = 2*rows - (x1 + x2)
 
    if y2 >= y1:
        y_value = y2 - y1
    else:
        y_value = 2*cols - (y1 + y2)
 
    ans = min(x_value, y_value)
    print(ans)