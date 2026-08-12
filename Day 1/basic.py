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

#Type Conversion -
d = "12"
e = int(d)
print(type(d))
print(type(e))

#boolean -
f= 22
g = 12.4
h = 0
i = ""
j = "Aher"
k = 0.0

print(bool(f))
print(bool(g))
print(bool(h))
print(bool(i))
print(bool(j))
print(bool(k))

#Input Output and Operators

l = input("What's your Name: ")
m = int(input("And your age: "))
print(f"So your name is {l} and you are {m} years old!")

# Operators -
# +	Addition	10 + 3	13
# -	Subtraction	10 - 3	7
# *	Multiplication	10 * 3	30
# /	Division	10 / 3	3.333…
# //	Floor Division	10 // 3	3
# %	Modulus (remainder)	10 % 3	1
# **	Exponentiation	2 ** 8	256

#Operator	Meaning	       Example	 Result
# ==	    Equal to	    5 == 5	 True
#!=	       Not equal to	    5 != 3	 True
# >	      Greater than	     5 > 3	 True
# <	       Less than	     5 < 3	 False
# >=	  Greater or equal	5 >= 5	 True
# <=	  Less or equal	    3 <= 5	 True

#Logical Operators
# Operator	    Returns True when…	             Example
# and	        Both conditions are True	     age > 18 and has_id == True
# or	        At least one condition is True	 is_admin or is_staff
# not	        Reverses the boolean	         not is_banned

###Assignment Operators

#Operator	  Meaning	             Equivalent to
# +=	   Add and assign	          x = x + n
# -=	  Subtract and assign	      x = x - n
# *=	  Multiply and assign	      x = x * n
# /=	  Divide and assign	          x = x / n
# //=	  Floor divide and assign	  x = x // n
# %=	  Modulus and assign	      x = x % n
# **=	  Power and assign	          x = x ** n

# +=
n = 12
if n != 21:
    n +=1
    print(n)
else:
    print("LOL!")

# -=
if n == 13:
    n -= 1
    print(n)
else:
    print("LOL!")

# *=
if n ==12:
    n *= 2
    print(n)
else:
    print("LOL!")

# /=
if n == 24:
    n /= 2
    print(n)
else:
    print("LOL!")

# //=
if n == 12.0:
    n //= 2
    print(n)
else:
    print("LOL!")

# **=
if n == 6.0:
    n ** 2
    print(n)
else:
    print("LOL!")

# %=
if n == 6.0:
    n %= 2
    print(n)
else:
    print("LOL!")

# Comparision Operators

'''
(==, <, >, <=, >=, !=)

Operator	Meaning	         Example	 Result
==	         Equal to	     5 == 5	     True
!=	       Not equal to	     5 != 3	     True
>	       Greater than	     5 > 3	     True
<	         Less than	     5 < 3	     False
>=	       Greater or equal	 5 >= 5	     True
<=	       Less or equal	 3 <= 5	     True

'''

# Logical Operators

'''
Operator	 Returns True when…	                Example
and	         Both conditions are True	        age > 18 and has_id == True
or	         At least one condition is True	    is_admin or is_staff
not	         Reverses the boolean	            not is_banned

'''


#### Conditional Statements ---

'''
Types at a Glance ....

Statement	      When to use it
if	              You have one condition to check
if-else	          Two paths — True or False
if-elif-else	  Multiple conditions checked one by one
'''

# Challenge -
#Q1. Accept two numbers and print the greatest between them.

o = int(input("Give me a number: "))
p = int(input("Give me a number: "))

if o == p:
    print("Both are same!")
elif o > p:
    print(f"Greater number is {o}")
elif o < p:
    print(f"Greater number is {p}")
else:
    print("Number is invalid!")

#Q2. Accept gender from user and print a greeting message.

q = str(input("What is your gender(M/F): ")).strip() .lower()
if q == "m":
    print("Good Morning Sir!")
elif q == "f":
    print("Good Morning Ma'am!")
else:
    print("Plz.. Choose the correct gender!")

#Q3. Accept an integer and check if it is even or odd.

r = int(input("Drop an Integer: "))
if r % 2 == 0:
    print("Even!")
else:
    print("Odd!")

# Q4. Accept name and age — check if the user is a valid voter (18+).

s = int(input("What's you age? : "))
if s >= 18:
    print(f"Hello {a}, you are valid voter!!")
elif s < 18:
    print(f"You may need to wait little more years until you can vote!!")
else:
    print("Your age must be 18 or above 18 to vote!")

#Q5. Accept a year and check if it is a leap year.

y = int(input("Enter the Year: "))
if (y % 4 == 0) and ((y % 400 == 0) or (y % 100 != 0)):
    print(f"{y} is an Leap Year!!")
else:
    print(f"{y} is not a Leap Year!")

# Q6 — Temperature Ladder Accept temperature in °C and print a description.

t = int(input("What's the Temperature in °C: "))
if t >= 40:
    print("I can feel the heat waves! 🔥")
elif t <= 39 and t >= 25:
    print("Pleasant 😊")
elif t <= 24 and t >= 8:
    print("It's chilly out there!")
elif t < 7:
    print("Freezing Cold 🥶")
else:
    print("plz take care!")
