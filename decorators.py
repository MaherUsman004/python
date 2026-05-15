def decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper  
@decorator
def greet():
    print("Hello, World!")

greet()
