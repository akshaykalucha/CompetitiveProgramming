x = int(input())
if x%5==0:
    print(x//5)
else:
    nn = x%5
    print(((x-nn)//5)+1)