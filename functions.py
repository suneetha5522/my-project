# differences between local and global variables:-
"""
Global Variable:-
a variable declared outside of the function is called global variable,this means, global variable can be accessed
inside or outside of the function.
"""

x = 100  # global variable


def hello():
    print("good morning")
    x = 20
    print("x is local inside function", x)  # global variable can be used as a local variable
    return x + x


hello()
print(hello())
print("x is global", x)

# converting global variable to local variable
x = 100  # global variable


def foo():
    print("modify global variable to local variable")
    global x
    x = 300  # initializing the global variable
    return x


x = foo()
print("global variable x:", x)

# Non local variable
x = 100


def wish():
    x = 200

    def hello1():
        nonlocal x  # creating the non local variable
        x = 300

    hello1()
    print("The non local variable:", x)
    return x


wish()
print("The global variable is :", x)

# how to swap two variables without using 3rd variable:-
x = 10
y = 5
x = x + y  # x now becomes 15

y = x - y  # y becomes 10

x -= y  # x becomes 5

y *= x  # y becomes 50

print("After Swapping: x =", x, " y =", y)


# Arbitary arguments with non key word arguments


def add(a, b):  # positional arguments
    return a + b


print("adding of two numbers:", add(4, 5))


def mul(c, d, e, f):  # keyword arguments
    return c * f


print("multiplication two numbers:", mul(d=10, f=20, c=12, e=46))


def sub(x, y, z=10):  # z is a default parameter
    return x - y - z


print("The substation of numbers:", sub(10, 6))
print("The substation of numbers:", sub(5, 30))


# Arbitrary Arguments:-
# example 1:-

def add(*x):
    return sum(x)


print("The addition of three numbers:", add(4, 5, 8))
print("The addition of n numbers:", add(1, 2, 3, 4, 5, 6, 7))


# Arbitrary Arguments with key word arguments:-

def person_details(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


person_details(Firstname="Suresh", Lastname="Kumar", Age=22, Phone=1234567890)
person_details(Firstname="naresh", Lastname="yadav", Email="nareshyadav@nomail.com", Country="india", Age=25, Phone=9876543210)
