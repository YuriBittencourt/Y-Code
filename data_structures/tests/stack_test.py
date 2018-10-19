from data_structures.stack import stack

my_stack = stack()
my_stack2 = stack()
print(my_stack==my_stack2)
my_stack.push("world")
print(my_stack==my_stack2)
my_stack2.push("world")
print(my_stack==my_stack2)
my_stack.push("bar")
my_stack.push("henlo")
my_stack.push("bar")
my_stack.push("foo")
my_stack.push("bar")
my_stack.push("bar")
my_stack2 = my_stack.copy()
print("joguei fora: ",my_stack.pop(),my_stack.pop())
print(len(my_stack), len(my_stack2))
print(my_stack == my_stack2)
print(len(my_stack))
print(my_stack.count("bar"))
while my_stack.has_next():
    print(my_stack.pop())
try:
    print(my_stack.pop())
except:
    print("Epa")
print("agr a 2")
while my_stack2.has_next():
    print(my_stack2.pop())
try:
    print(my_stack2.pop())
except:
    print("Epa")


print(len(my_stack))
print(len([0,1]))
