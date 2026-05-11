# sets are collection of unique value items . there is no order in sets and they are mutable .
#  they are defined using curly braces {} or the set() constructor. 
set1 = {"apple", "apple" ,"banana", "cherry"}
print(set1)

set2 = {}
print(type(set2)) # this creates an empty dictionary, not a set

set3 = set()
print(type(set3)) # this creates an empty set

# how acess elements in a set ? we can't use index method instead use for loop 
s1 = {"apple", "banana", "cherry" , 11, 22, 33 ,5.14 ,True}
for item in s1:
    print(item)

# methods or operations on sets 

# add method adds an element to the set
s1 = {"apple", "banana", "cherry" , 11, 22, 33 ,5.14 ,True}
print(f"{s1} before adding orange")
s1.add("orange")
print(f"{s1} after adding orange")
# to add literals to a set we can use update method
s1.update(["grape", "melon"])
print(f"{s1} after updating with grape and melon")

# remove method removes the specified element from the set. if the element is not present,  
#  it raises a KeyError
s1.remove("banana")
print(f"{s1} after removing banana")

# discard method removes the specified element from the set. if the element is not present, it does nothing
s1.discard(11) 
s1.discard("grape ") # this will not raise an error because discard does not raise an error if the element is not present
print(f"{s1} after discarding 11")

# pop method removes and returns an arbitrary(not specified(random element)) from the set. if the set is empty, it raises a KeyError
popped_item = s1.pop()
print(f"{s1} after popping an element: {popped_item}")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}  
# union method returns a new set that contains all the elements from both sets
union_set = set1.union(set2)    
print(f"Union of set1 and set2: {union_set}")

# join tuple and a set using union method 
x = (1, 2, 3)
y = {4, 5, 6}
z = y.union(x)
print(f"Union of tuple x and set y: {z}")

# unionupdate method updates the set with the union of itself and another set
# set1.update(set2)
# print(f"set1 after union update with set2: {set1}")
# this change original set1 to the union of set1 and set2

intersection_set = set1.intersection(set2)
print(f"Intersection of set1 and set2: {intersection_set}")

# intersection_update method updates the set with the intersection of itself and another set   
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
a.intersection_update(b)
print(f"Set a after intersection update with set b: {a}")

cities = {"New York", "Los Angeles", "Chicago", "Houston", "Phoenix"}
cities2 = {"Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio"}
# difference method returns a new set that contains the elements that are in the first set but not in the second set
difference_set = cities.difference(cities2)
print(f"Difference of cities and cities2: {difference_set}")
# check if a city is in the set 
city_to_check = "Chicago"
if city_to_check in cities:
    print(f"{city_to_check} is in the set of cities.")
 
# symmetric-difference method returns a new set that contains the elements that are in either set but not in both sets 
symmetric_difference_set = cities.symmetric_difference(cities2)
print(f"Symmetric difference of cities and cities2: {symmetric_difference_set}")