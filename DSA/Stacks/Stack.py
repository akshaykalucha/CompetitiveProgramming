class Stack:
    def __init__(self, n):
        self.n = n
        self.stack = [0]*n
    
    def getSize(self):
        if sum(self.stack) > 0:
            c = 0
            for i in range(self.n):
                if self.stack[i] != 0:
                    c+=1
                else:
                    break
            return c
        else:
            return 0
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def isFull(self):
        return self.getSize() == self.n
    
    def push(self, element):
        if self.isFull():
            return False
        filledTill = self.getSize()-1
        self.stack[filledTill+1] = element
        
    def pop(self):
        if self.isEmpty():
            return False
        filledTill = self.getSize()
        top = self.stack[filledTill-1]
        self.stack[filledTill-1] = 0
        return top
    
    def peek(self, position):
        if self.isEmpty():
            return False
        return self.stack[position]
    
    def searchElPos(self, element):
        if self.isEmpty():
            return False
        try:
            index = self.stack.index(element)
            return index
        except ValueError:
            return False
    
    def display(self):
        return self.stack
        