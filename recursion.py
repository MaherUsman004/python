def factorial(n):
    if n==1:
        return 1
    else:
        return n* factorial(n-1)
    
factorial(5)

# program to find the nth Fibonacci number using recursion 
def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
     return fibonacci(n-1) + fibonacci(n-2)

fibonacci(6)

# Sum of First n Numbers
def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)
    
number = int(input("Enter a number: "))
print(f"The sum of the first {number} numbers is: {sum(number)}")
