class Nodo():
    def __init__(self,dato):
        self.elemento = dato
        self.next = None
class Lista():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def print(self):
        temp = self.head
        while(temp != None):
            print(temp.elemento)
            temp = temp.next
    def append(self,dato):
        nodo = Nodo(dato)
        if self.length == 0:
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.next = nodo
            self.tail = nodo
        self.length += 1