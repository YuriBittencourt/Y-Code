class linked_list:
    def __init__(self, max_capacity=None):
        self.__max_capacity = max_capacity
        self.__first = None
        self.__size = 0

    def is_full(self):
        if self.__max_capacity is not None and self.__size == self.__max_capacity:
            return True
        return False

    def is_empty(self):
        if self.__first is None:
            return True
        return False

    def insert(self, item):
        if self.is_full():
            raise ValueError("list is full")

        if self.is_empty():
            self.__first = [item, None]
            self.__size += 1
            return
        next_node = self.__first
        while next_node[1] is not None:
            next_node = next_node[1]
        next_node[1] = [item, None]
        self.__size += 1

    def __str__(self):
        res = []
        iter = self.__first
        while type(iter) == type(list()):
            res.append(iter[0])
            iter = iter[1]
        return "[" + ",".join(res) + "]"
