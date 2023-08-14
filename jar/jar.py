class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Can't be a negative number")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too Much")
        if n > self.capacity:
            raise ValueError("Too Much")
        self.size = self.size + n

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size