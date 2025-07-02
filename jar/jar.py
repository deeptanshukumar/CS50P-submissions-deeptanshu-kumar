class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if self.size+n>self.capacity:
            raise ValueError("exceeding capacity of the jar!")
        else:
            self.size+=n

    def withdraw(self, n):
        if self.size-n<0:
            raise ValueError("not enough cookies!")
        else:
            self.size-=n

    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, capacity):
        if capacity<0:
            raise ValueError("capacity cant be negative!")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size<0:
            raise ValueError("size cant be negative!")
        self._size = size
