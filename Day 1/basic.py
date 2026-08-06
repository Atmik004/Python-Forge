print("Hello, Atmik!")
# This is a simple Python program that prints what is inside the quotation marks.

# - is denoted as a comment in Python. It is used to explain what the code does.

## Variables are used to store data in Python. In this case, we are storing the string "Atmik"
first_name = "Atmik"
print(first_name) #this line will print the value of the variable first_name, which is "Atmik".

Atmik = 15
age = 22.1

# variable can be stored in many other formats like Number, boolane, float, etc
#camelCase  → myVariableName
atmikAher = 23
#PascalCase → MyVariableName
AtmikAher = 24
#snake_case → my_variable_name   ✅ Python prefers this
Atmik_Aher = 25

# Data Types -

print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>

#String -
a = "Atmik"
print(a[0], a[-5])
#Slice Function-
print(a[0:3:1])
b = "COLLEGE"
print(b[0:8:2])
#Defalt Values -
print(b[::2])

c = "Hellow how are you"
#print how
print(c[7:10:1])
#print you
print(c[15::1])
#print Hellow
print(c[:6:1])

print(c[::-1])