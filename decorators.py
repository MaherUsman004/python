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
 
#  *args  and **kwargs 
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result
print(multiply(2,3,4))
    
def profile(name , *skills , **info):
    print("name is :" , name)
    print("skills :", skills)
    print(" more info:", info)

data =profile("usman" , "pthon" ,"Reactjs" , age=21,city="Lahore")
print(data)

# decorator with arguments
def decorator_function(original_function):
    def wrapper(*args,**kwags):
        print("before execution")
        original_function(*args,**kwags)
        print("after execution")
    return wrapper

@decorator_function
def sum(a,b,c):
    print("the sum is :" , a+b+c) 
sum(2,3,4)  

# program to calculate execution time of a function using decorator
import time  

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper  

@timer  
def slow_function():
    time.sleep(2)  
slow_function()