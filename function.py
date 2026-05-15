def greet(name):
    return f"Hello, {name}!"
print(greet("alice"))

def fahrenheit_to_celsius(fahrenhiet):
    return (fahrenhiet - 32) * 5 / 9

temp = float(input("Enter temperature in Fahrenheit: "))
print(f"Temperature in Celsius: {fahrenheit_to_celsius(temp)}")

def gmean(a,b):
    mean = (a * b)/(a + b)
    return mean
print(gmean(4, 5))

# lambda functions are anonymous functions that can have any number of arguments but only one expression. They are often used for short, simple functions that are not reused elsewhere in the code.

square = lambda x: x ** 2
print(square(5))

