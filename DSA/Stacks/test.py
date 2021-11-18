from Stack import Stack

name = Stack(6)
spell = [1,2,3]
for el in spell:
    name.push(el)
print(name.display())
print(name.getSize())