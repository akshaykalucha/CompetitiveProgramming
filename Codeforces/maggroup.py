n=int(input())
counter=0
t=[]
while counter<n:
    a=int(input())
    t.append(a)
    counter+=1
i=0
pieces=1 
while i<n-1:
    if t[i]!=t[i+1]:
        pieces+=1 
    i+=1
print(pieces)