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
        if self.is_empty():
            self.__next = [item, None]
            self.__size += 1
            return
        aux = self.__next
        while aux[1] is not None:
            aux = aux[1]
        aux[1] = [item, None]
        self.__size += 1

    def dequeue(self):
        if self.is_empty():
            raise(ValueError("Stack is empty"))
        aux = self.__next[0]
        self.__next = self.__next[1]
        self.__size -= 1
        return aux

    def peek(self):
        if self.is_empty():
            return None
        return self.__next[0]

    def clear(self):
        self.__next = None
        self.__size = 0

    def reverse(self):
        if not self.is_empty():
            item = self.dequeue()
            self.reverse()
            self.enqueue(item)

    def count(self, element):
        res = 0
        items = []
        while not self.is_empty():
            items.append(self.dequeue())
            if items[-1] == element:
                res += 1
        for item in items:
            self.enqueue(item)
        return res

