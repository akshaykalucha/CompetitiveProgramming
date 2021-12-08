r, c = [int(i) for i in input().split()]
 
rows_eaten = 0
cake = []
for i in range(r):
    s = input()
    cake.append(s)
    if "S" not in s:
        rows_eaten += 1
 
columns_eaten = 0
for i in range(c):
    for j in range(r):
        if cake[j][i] == "S":
            break
    else:
        columns_eaten += 1
 
 
pieces = (c - columns_eaten) * rows_eaten
pieces += columns_eaten * r
 
print(pieces)