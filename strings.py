str = "hello, WORLD!"
print(str[0])
print(str[7])

print(str[-1])
print(str[-6])

# .len()mehthod
print(len(str))

# string slicing
print(str[0:6])
print(str[7:13])

# .upper() and .lower() methods
print(str.upper()[0:6])
print(str.lower()[7:13])

name = " hello  "
print(name.strip())

# .replace() method
print(name.replace("hello","world"))

# .split() method
fruits = "apple, banana, cherry"
fruit_list = fruits.split(", ")
print(fruit_list)



# Summary Table
# Method	Purpose
# upper()	Capital letters
# lower()	Small letters
# strip()	Remove spaces
# replace()	Replace text
# find()	Find position
# split()	Break into list
# len()	    Length
# count()	Count characters