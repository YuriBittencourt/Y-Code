from data_structures.stack import stack
import copy
from random import random, randint

if __name__ == "__main__":
    print("-" * 50, "\nRunning the stack constructor test case")
    try:
        my_stack = stack()
        assert type(my_stack) == stack
        size = int(random()*10+1)
        my_stack2 = stack(size)

        try:
            stack(int(random() * -10))
            print("Failed!")

        except ValueError:
            print("Passed!")

    except AssertionError:
        print("Failed!")

    print("-" * 50, "\nRunning the get_max_capacity method test case")
    try:
        assert my_stack.get_max_capacity() is None
        assert my_stack2.get_max_capacity() == size
        print("Passed!")
    except AssertionError:
        print("Failed!")

    print("-" * 50, "\nRunning the is_empty and is_full method test case")
    try:
        my_stack2 = stack(1)
        assert my_stack2.is_empty()
        assert not my_stack2.is_full()
        my_stack2.push(None)
        assert not my_stack2.is_empty()
        assert my_stack2.is_full()
        print("Passed!")
    except AssertionError:
        print("Failed!")

    print("-" * 50, "\nRunning the push and pop method test case")
    try:
        item = "SOMETHING"
        my_stack.push(item)
        assert my_stack.pop() == item
        my_stack = stack(randint(1, 25))
        i = 0
        while not my_stack.is_full():
            my_stack.push(i)
            i += 1
        assert my_stack.get_max_capacity() == len(my_stack) and i == my_stack.get_max_capacity()
        while not my_stack.is_empty():
            my_stack.pop()
            i -= 1
        assert len(my_stack) == i and i==0
        print("Passed!")
    except AssertionError:
        print("Failed!")

    print("-" * 50, "\nRunning the len method test case")
    try:
        assert my_stack2.is_full() and len(my_stack2) == my_stack2.get_max_capacity()
        assert my_stack.is_empty() and len(my_stack) == 0
        print("Passed!")
    except AssertionError:
        print("Failed!")

    print("-" * 50, "\nRunning the top and has_next method test case")
    try:
        assert my_stack.top() is None
        assert not my_stack.has_next()
        my_stack.push(item)
        assert my_stack.top() == item
        my_stack.push(item)
        assert my_stack.has_next()
        print("Passed!")
    except AssertionError:
        print("Failed!")

    print("-" * 50, "\nRunning the clear method test case")
    try:
        assert not my_stack.is_empty()
        assert my_stack.top() is not None
        my_stack.clear()
        assert my_stack.top() is None
        assert len(my_stack) == 0
        assert my_stack.is_empty()
        print("Passed!")
    except AssertionError:
        print("Failed!")

    print("-" * 50, "\nRunning the reverse method test case")
    try:
        my_stack = stack()
        my_stack.reverse()
        assert my_stack == stack()
        lst = ['a', 1, [], ('a', 'b'), {}]
        for i in lst:
            my_stack.push(i)
        assert len(lst) == len(my_stack)
        my_stack.reverse()
        for i in lst:
            assert i == my_stack.pop()
        print("Passed!")
    except AssertionError:
        print("Failed!")

    print("-" * 50, "\nRunning the remove_ocurrences and \nremove_all_ocurrences method test case")
    try:
        qnty = 100
        item2 = "Dummy"
        for _ in range(0,qnty):
            my_stack.push(item)
            my_stack.push(item2)
        assert my_stack.count(item) == qnty
        my_stack.remove_ocurrences(item)
        assert my_stack.count(item) == qnty-1
        assert my_stack.top() != item
        my_stack.remove_ocurrences(item, qnty-1)
        my_stack.remove_all_ocurrences(item2)
        assert my_stack.is_empty()
        print("Passed!")
    except AssertionError:
        print("Failed!")

    print("-" * 50, "\nRunning the contains method test case")
    try:
        assert item not in my_stack
        my_stack.push(item)
        assert item in my_stack
        print("Passed!")
    except AssertionError:
        print("Failed")

    print("-" * 50, "\nRunning the copy and deepcopy method test case")
    try:
        item = ["Nugget","Biscuit"]
        my_stack.push(item)
        cpy_stack = copy.copy(my_stack)
        assert my_stack == cpy_stack
        item.append("Mashed Potatoes")
        assert my_stack.top() == item
        assert my_stack == cpy_stack
        cpy_stack = copy.deepcopy(my_stack)
        assert cpy_stack == my_stack
        item.remove("Biscuit")
        assert not cpy_stack == my_stack
        print("Passed!")
    except AssertionError:
        print("Failed")

    print("-" * 50, "\nRunning the equality method test case")
    try:
        item = 666
        my_stack = stack()
        my_stack2 = stack()
        assert my_stack == my_stack2
        for _ in range(0, 10):
            my_stack.push(item)
            my_stack.push(item / 2)
            my_stack2.push(item)
            my_stack2.push(item / 2)

        while not my_stack.is_empty():
            assert my_stack.pop() == my_stack2.pop()
        print("Passed!")
    except AssertionError:
        print("Failed")
