import copy


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

    def to_list(self):
        lst = []
        while not self.is_empty():
            lst.append(self.dequeue())
        for item in lst:
            self.enqueue(item)
        return lst

    def remove_ocurrences(self, element, ocurrencies=1):
        if ocurrencies < 1:
            raise ValueError("Invalid number of ocurrencies, must be equal or greater than 1, inserted:", ocurrencies)
        lst = self.to_list()
        if element not in lst:
            return
        for i in lst:
            if i == element:
                lst.remove(i)
                ocurrencies -= 1
                if ocurrencies == 0:
                    break
        self.clear()
        for i in lst:
            self.enqueue(i)

    def remove_all_ocurrences(self, element):
        lst = self.to_list()
        if element not in lst:
            return
        for i in lst:
            if i == element:
                lst.remove(i)
        self.clear()
        for i in lst:
            self.enqueue(i)

    def __contains__(self, element):
        lst = self.to_list()
        if element in lst:
            return True
        return False

    def __copy__(self):
        cpy = queue(self.get_max_capacity())
        lst = self.to_list()
        for i in lst:
            cpy.enqueue(i)
        return cpy

    def __deepcopy__(self):
        cpy = queue(self.get_max_capacity())
        lst = self.to_list()
        for i in lst:
            cpy.enqueue(copy.deepcopy(i))
        return cpy

    def __eq__(self, other):
        if (other is None or
            self.get_max_capacity() != other.get_max_capacity() or
                len(self) != len(other)):
            return False
        return self.__eq(other)

    def __eq(self, other):
        self_contents = self.to_list()
        other_contents = other.to_list()
        if self_contents == other_contents:
            return True
        return False
