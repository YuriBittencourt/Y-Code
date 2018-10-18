class stack:
    def __init__(self, max_capacity=None):
        if max_capacity is not None and max_capacity <1:
            raise ValueError("Expected a value greater than 0")
        self.__first = None
        self.__size = 0
        self.__max_capacity = max_capacity

    def get_size(self):
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

    #TODO quebrar essa recursão ou algo que retire o __val
    def count(self, element, __val=0):
        if self.is_empty():
            return __val
        if self.has_next():
            item = self.pop()
            if item == element:
                __val += 1
            __val = self.count(element, __val)
            self.push(item)
        return __val


my_stack = stack()
my_stack.push("world")
my_stack.push("bar")
my_stack.push("henlo")
my_stack.push("bar")
my_stack.push("foo")
my_stack.push("bar")
print(my_stack.count("bar"))
my_stack.reverse()
while my_stack.has_next():
    print(my_stack.pop())
try:
    print(my_stack.pop())
except:
    print("Epa")

print(my_stack.get_size())
print(len([0,1]))
