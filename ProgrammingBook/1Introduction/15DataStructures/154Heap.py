class OurHeap:
    def __init__(self, items):
        self.heap = [None] # index 0 will be ignored self.rank = {}
        for x in items:
            self.push(x) 
        
    def __len__(self):
        return len(self.heap) - 1
    
    