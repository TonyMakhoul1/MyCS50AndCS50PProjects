class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Can't be a negative number")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Too Much")
        if n > self.capacity:
            raise ValueError("Too Much")
        self._size = self._size + n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Negative Number")
        if self._size - n < 0:
            raise ValueError("We Don't Have Enough Cookies")
        self._size = self._size - n
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(3)
jar.withdraw(2)
print(jar)