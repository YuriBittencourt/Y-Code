class stack:
    def __init__(self, max_capacity=None):
        if max_capacity is not None and max_capacity <1:
            raise ValueError("Expected a value greater than 0")
        self.__first = None
        self.__size = 0
        self.__max_capacity = max_capacity

    def __len__(self):
        return self.__size

    def get_max_capacity(self):
        return self.__max_capacity

    def is_empty(self):
        if self.__first is None:
            return True
        return False

    def is_full(self):
        if self.__max_capacity is not None and self.__size == self.__max_capacity:
            return True
        return False

    def has_next(self):
        if not self.is_empty() and self.__first[1]:
            return True
        return False

    def push(self, item):
        if self.is_full():
            raise(OverflowError("Stack is full, could not put", item))
        self.__first = (item, self.__first)
        self.__size += 1

    def pop(self):
        if self.is_empty():
            raise(ValueError("Stack is empty"))
        self.__size -= 1
        popped = self.__first[0]
        self.__first = self.__first[1]
        return popped

    def top(self):
        if self.is_empty():
            return None
        return self.__first[0]

    def clear(self):
        self.__first = None
        self.__size = 0

    #TODO melhorar
    def reverse(self):
        if not self.is_empty():
            temp = self.pop()
            self.reverse()
            self.__insert_at_bottom(temp)

    def __insert_at_bottom(self, aux):
        if self.is_empty():
            self.push(aux)
            return
        temp = self.pop()
        self.__insert_at_bottom(aux)
        self.push(temp)

    def count(self, element):
        res = 0
        if self.is_empty():
            return res
        if self.has_next():
            item = self.pop()
            if item == element:
                res += 1
            res += self.count(element)
            self.push(item)
        return res

    #Todo create copy
    def copy(self):
        cpy = stack(self.get_max_capacity())
        aux = []
        while not self.is_empty():
            aux.append(self.pop())

        while aux:
            item = aux.pop()
            cpy.push(item)
            self.push(item)
        return cpy

    #Todo create deepcopy
    def __deepcopy__(self, memodict={}):
        raise NotImplementedError

    def __eq__(self, other):
        if self.is_empty() and other.is_empty():
            return True
        if (self.is_empty() and not other.is_empty()) or \
            (not self.is_empty() and other.is_empty()) or \
            self.top() != other.top():
            return False
        item_a = self.pop()
        item_b = other.pop()
        equity = self.__eq__(other)
        self.push(item_a)
        other.push(item_b)
        return equity
