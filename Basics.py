# print("Hello, World!")
# a = 5
# b = 10
# sum = a + b
# print(sum)
correct_password = 1234
correctname = "admin"
name = str(input("What is your name?"))
password = int(input("What is your password? "))
if name == correctname and password == correct_password:
    print("PASSWORD is correct, welcome admin!")
    marks = int(input("Enter your marks: "))
    if marks >=90:
        print("GRADE A")
    elif marks >=80:
        print("GRADE B")
    elif marks >=60:
        print("GRADE c")
    elif marks >=40:
        print("GRADE D")
    else:
        print("FAILED")
else:
    print("Incorrect password, access denied.")
  
