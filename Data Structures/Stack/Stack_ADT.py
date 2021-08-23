# Completed implementation of a stack ADT
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):                     # tests to see whether the stack is empty
        return self.items == []
    
    def push(self, item):                   # adds a new item to the top of the stack
        self.items.insert(0, item)
        
    def pop(self):                          # removes the top item from the stack
        return self.items.pop(0)
    
    def peek(self):                         # returns the top item from the stack
        return self.items[0]
    
    def size(self):                         # returns the number of items on the stack
        return len(self.items)
