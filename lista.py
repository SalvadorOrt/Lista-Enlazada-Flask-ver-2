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
        cadena = ''
        temp = self.head
        while(temp != None):
            cadena += str(temp.elemento) + ' '
            print(temp.elemento)
            temp = temp.next
        return cadena
    def append(self,dato):
        nodo = Nodo(dato)
        if self.length == 0:
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.next = nodo
            self.tail = nodo
        self.length += 1
    def prepend(self,dato):
        nodo = Nodo(dato)
        if self.length == 0:
            self.head = nodo
            self.tail = nodo
        else:
            nodo.next = self.head
            self.head = nodo
        self.length +=  1
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next != None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.elemento
    def prepop(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.elemento