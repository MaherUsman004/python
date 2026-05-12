student = {
    "name": "usman",
    "age": 20,
    "age": 40,      
    # duplicate value will overwrite the previous value so now age is 40 not 20
    "course": ["python", "java", "c++"]
}
student["rollno"] = 12345
print(student)
print(student.get("name"))
print(student.get("age"))
print(student.get("course"))
print(student.get("rollno"))

# using dict() constructor
car = dict(make = "Toyota", model = "Camry", year = 2020 , color = ["red" , "blue", "black"])
print(car)

print(car.keys())
car["color"].append("white")
car["year"] = 2021
print(car)

# removing items 
car = dict(make = "Toyota", model = "Camry", year = 2020 , color = ["red" , "blue", "black"])
car.pop("model") 
# this will remove the key "model" and its value from the dictionary
print(car)
del car["year"]
# this will remove the key "year" and its value from the dictionary
print(car)
car.clear()
print(type(car))


# program1 "count number of words in s string and make a dictionary"
text = "python is easy and python is powerful"
words = text.split()
frequency ={}
for word in words:
    if word in frequency:
        frequency[word] +=1
    else:
       frequency[word] =1
print(frequency)

# program2 Student Marks Analyzer
marks = {
    "Rahul": 85,
    "Anita": 92,
    "John": 78,
    "Priya": 90
}
total_marks = sum(marks.values())
average_marks = total_marks / len(marks)
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")    
highest_marks = max(marks.values())
lowest_marks = min(marks.values())
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")  

# program3 "Innerted a dictionary 
data = {"a": 1, "b": 2, "c": 1}

inverted_data = {}

for key, value in data.items():
    if value not in inverted_data:
        inverted_data[value] = [key]   # always store list
    else:
        inverted_data[value].append(key)

print(inverted_data)

# program
d1 = {"a": 100, "b": 200}
d2 = {"b": 300, "c": 400}
result = d1.copy()
for key , value in d2.items():
    if key in result :
       result[key] += value
    else:
          result[key] = value

print(result)