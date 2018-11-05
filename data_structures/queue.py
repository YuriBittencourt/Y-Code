class queue:
    def __init__(self, max_capacity=None):
        if max_capacity is not None and max_capacity <1:
            raise ValueError("Expected a value greater than 0")
        self.__next = None
        self.__size = 0
        self.__max_capacity = max_capacity

    def __len__(self):
        return self.__size

    def get_max_capacity(self):
        return self.__max_capacity

    def is_empty(self):
        if self.__next is None:
            return True
        return False

    def is_full(self):
        if self.__max_capacity is not None and self.__size == self.__max_capacity:
            return True
        return False

    def has_next(self):
        if not self.is_empty() and self.__next[1]:
            return True
        return False

    def enqueue(self, item):
        if self.is_full():
            raise (OverflowError("Stack is full, could not put", item))
        # TODO CREATE ME
        pass

    def dequeue(self):
        if self.is_empty():
            raise(ValueError("Stack is empty"))
        # TODO CREATE ME
        pass