import copy

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

    def reverse(self):
        temp = []
        while not self.is_empty():
            temp.append(self.pop())

        while temp:
            self.push(temp.pop(0))

    def count(self, element):
        res = 0
        if not self.is_empty():
            item = self.pop()
            if item == element:
                res += 1
            res += self.count(element)
            self.push(item)
        return res

    def remove_ocurrences(self, element, ocurrencies=1):
        if ocurrencies < 1:
            raise ValueError("Invalid number of ocurrencies, must be equal or greater than 1, inserted:", ocurrencies)
        if not self.is_empty():
            item = self.pop()
            if item != element:
                self.remove_ocurrences(element, ocurrencies)
                self.push(item)
            else:
                if ocurrencies == 1:
                    return
                self.remove_ocurrences(element, ocurrencies-1)

    def remove_all_ocurrences(self, element):
        if not self.is_empty():
            item = self.pop()
            self.remove_all_ocurrences(element)
            if item != element:
                self.push(item)

    def __contains__(self, element):
        retval = False
        if not self.is_empty():
            item = self.pop()
            if item == element:
                self.push(item)
                return True
            retval = element in self
            self.push(item)
        return retval

    def __copy__(self):
        cpy = stack(self.get_max_capacity())
        aux = []
        while not self.is_empty():
            aux.append(self.pop())

        while aux:
            item = aux.pop()
            cpy.push(item)
            self.push(item)
        return cpy

    def __deepcopy__(self, memodict={}):
        cpy = stack(self.get_max_capacity())
        aux = []
        while not self.is_empty():
            aux.append(self.pop())

        while aux:
            item = aux.pop()
            cpy.push(copy.deepcopy(item))
            self.push(item)
        return cpy

    def __eq__(self, other):
        if other is None or \
                self.get_max_capacity() != other.get_max_capacity() or \
                len(self) != len(other):
            return False
        return self.__eq(other)

    def __eq(self,other):
        if self.is_empty() and other.is_empty():
            return True
        if (self.is_empty() and not other.is_empty()) or \
            (not self.is_empty() and other.is_empty()) or \
                self.top() != other.top():
            return False
        item_a = self.pop()
        item_b = other.pop()
        equity = self.__eq(other)
        self.push(item_a)
        other.push(item_b)
        return equity
