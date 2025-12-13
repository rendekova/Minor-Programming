class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            # If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        # return a str with 𝑛 🍪, where 𝑛 is the number of cookies in the cookie jar.
        return "🍪" * self._size


    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Must deposit a non-negative integer number of the cookies.")
        if self._size + n > self._capacity:
            # If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
            raise ValueError("Deposit exceeds jar capacity.")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Must withdraw a non-negative integer number of the cookies.")
        if n > self._size:
            # If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
            raise ValueError("Not enough cookies in the jar to withdraw.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

