class Stack:
    
    def __init__(self):
        self.item = list()

    def isEmpty(self):

        return self.item == []
        

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def size(self):

        return len(self.item)
