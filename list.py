mylist = ["apple", "banana", "cherry"]
print(mylist)

# list indexing
print(mylist[0])
print(mylist[1])
print(mylist[2])

# list slicing
print(mylist[0:2])
print(mylist[1:3])

# list methods
mylist.append("orange")
print(mylist)

# insertion method
mylist.insert(1, "grape")
print(mylist)

#  remove method remove first occurrence of the specified value
mylist.remove("banana")
print(f"{mylist} after removing banana")

# pop method removes the item at the specified position in the list and returns it
popped_item = mylist.pop(2)
print(f"popped item at index 2: {popped_item}")
print(f"{mylist} after popping item at index 2")

# sort method sorts the list in ascending order
mylist.sort()
print(f"{mylist} after sorting")

# reverse method reverses the order of the list
mylist.reverse()
print(f"{mylist} after reversing")

# extend method adds the elements of a list (or any iterable), to the end of the current list 
mylist.extend(["kiwi", "melon"])
print(f"{mylist} after extending with ['kiwi', 'melon']")

# list comprehension
squares = [x**2 for x in range(1, 11)]
print(f"Squares of numbers from 1 to 10: {squares}")