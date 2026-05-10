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