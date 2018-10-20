from data_structures.stack import stack
import copy
my_stack = stack()
my_stack2 = stack()
print(my_stack==my_stack2)
my_stack.push("world")
print(my_stack==my_stack2)
my_stack2.push("world")
print(my_stack==my_stack2)
my_stack.push("henlo")

my_stack2 = copy.copy(my_stack)
print(len(my_stack), len(my_stack2))
print(my_stack == my_stack2)
print(len(my_stack))
print(my_stack.count("bar"))
my_stack.reverse()
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
this = ["holy","cow"]
my_stack.push(this)
my_stack2 = copy.deepcopy(my_stack)
this.append("hey")
print(this, my_stack.top(), my_stack2.top())

my_stack = stack()
alt = True
for _ in range(10):
    my_stack.push("banana")
    my_stack.push("maçã")
    if alt:
        my_stack.push("abacaxi")
        alt = False
    else:
        alt= True

print("maçã:",my_stack.count("maçã"), "banana:", my_stack.count("banana"), "abacaxi:", my_stack.count("abacaxi"))

print("-"*50)

my_stack.remove_all_ocurrences("maçã")
my_stack.remove_ocurrences("banana")
my_stack.remove_ocurrences("abacaxi")

print("maçã:",my_stack.count("maçã"), "banana:", my_stack.count("banana"), "abacaxi:", my_stack.count("abacaxi"))


print("maçã" in my_stack)