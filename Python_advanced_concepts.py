'''
Here in this script , I am going to implement advance concepts of the python language which are more lenient towards 
Software Engineering concepts. We want to write code which is more readable, scaleable, reuseable and to achieve this
we have to use concepts like decorators, functional, Dunders, Magic methods, lambda, list comprehensions etc. 

Lets began our Journey ! 
'''
# Dunders-> double underscore methods like __init__()

class Person:
    def __init__(self, name, age):
        self.name = name

        self.age = age 
    def __del__(self):
        print("object is being Destroyed")

P = Person("mike", 15)

# use operator overloading to be able to perform arthematic operations on objects of Vector class
# If you want to represent the vector, then we use __repr__() 

class Vector:

    def __init__(self, x, y):
        
        self.x = x

        self.y = y

    def __add__(self, other):

        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):

        return f"X: {self.x}, Y: {self.y}"

    def __len__(self):
        return 10

    def __call__(self):
        
        print("I am the object and I was called")

v1 = Vector(10,20)

v2= Vector (50, 60)

v3 = v1 + v2

print(v3.x)
print(v3.y)

print(v3)
print(len(v3))
v3()
v1()
v2()

# Decorators: add some different functionality to other function

def myDecorator(function):

    def wrapper(*args, **kwargs):
        print("I am decorating thei function ")
        return_value = function(*args, **kwargs)

        return return_value
        

    return wrapper

@myDecorator
def hello_myWorld(person):
    #print("Hello world !", person )
    return f"hello {person}"



print(hello_myWorld("Mike"))


# Generators 

# if we wantto create sequence of number from 1 to 10 million then normally we can use range function in forloop but range() has some limitation
# this is where we use generators which will give use the vlaue of sequence on DEMAND

def myGenerator(n):

    for x in range(n):
        yield x**3

values = myGenerator(90000000)


# every values call function and produces next value
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

