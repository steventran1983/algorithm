class Stack():
    def __init__(self):
     self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_Empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False




        
            
    