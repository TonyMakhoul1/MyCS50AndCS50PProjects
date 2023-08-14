class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Can't be a negative number")
        self.capacity = capacity

    def __str__(self):
        return "🍪" * n

    def deposit(self, n):
        

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...