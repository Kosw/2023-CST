class integer:
    def __init__(self, x):
        self.x = int(x)
    
    def __add__(self, y):
        return self.x + int(y)
    
    def __sub__(self, y):
        return self.x - int(y)