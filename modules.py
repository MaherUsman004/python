import math 
print(math.sqrt(16))
print(math.pi)
print(math.factorial(5))
print(math.gcd(12, 15))
print(math.sin(math.pi/2))
print(math.cos(0))
x = 5.7
print(math.ceil(x))
print(math.floor(x))
y = 2.3
print(min(x,y))
print(max(x,y))
print(math.pow(2,3))


#random module
import random
print(random.randint(1, 10))  #print random number from 1 to 10
print(random.choice(['apple', 'banana', 'cherry']))  #print random element from the list
print(random.random())  #print random float between 0 and 1
print(random.uniform(1.0, 10.0))  #print random float between 1.0 and 10.0

# password genwrator using random module
import string
import random
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))
print(generate_random_string(8))

