class FIFO():
    def __init__(self, *args):
        if len(args) == 0:
            self.fifo = []
        elif type(args[0]) == list:
            self.fifo = args[0]
        else:
            self.fifo = list(args)

    def push(self, x:int):
        self.fifo.append(x)

    def pop(self):
        if len(self.fifo) > 0:
            return self.fifo.pop(0)
        else:
            return None
    
class LIFO():
    def __init__(self, *args):
        if len(args) == 0:
            self.lifo = []
        elif type(args[0]) == list:
            self.lifo = args[0]
        else:
            self.lifo = list(args)

    def push(self, x:int):
        self.lifo.append(x)

    def pop(self):
        if len(self.lifo) > 0:
            return self.lifo.pop()
        else:
            return None
        
class LILO():   # LILO <=> FIFO
    def __init__(self, *args):
        if len(args) == 0:
            self.lilo = []
        elif type(args[0]) == list:
            self.lilo = args[0]
        else:
            self.lilo = list(args)

    def push(self, x:int):
        self.lilo.append(x)

    def pop(self):
        if len(self.lilo) > 0:
            return self.lilo.pop(0)
        else:
            return None
