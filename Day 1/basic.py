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

# Loops

# For Loop

'''
The range() Function
range() generates a sequence of numbers. Think of it as saying "count from here to there".

range(stop)              # 0 up to stop-1
range(start, stop)       # start up to stop-1
range(start, stop, step) # start, jumping by step

list(range(5))           # [0, 1, 2, 3, 4]
list(range(1,6))         # [1, 2, 3, 4, 5]
list(range(0,10,2))      # [0, 2, 4, 6, 8]
'''


#For Loop with Numbers
for i in range(1, 6):
    print(i)

# Output: 1  2  3  4  5


# Q. Print 5's table using for loop
for i in range(5,51,5):
    print(i)

# Q. Table for give number
u = int(input("What table do you want: "))
for i in range(u, (u*10)+1, u):
    print(u)


name = "Atmik"
# Method 1 — via index
for i in range(len(name)):
    print(name[i])

# Method 2 — direct (simpler!)
for char in name:
    print(char)

# Method 3 - Manual.
for i in range(len(a)):
    print(f"{i} : {a[i]}")


#📝 For Loop Questions

#Q1. Print "Hello World" n times.
#r = int(input("How many times do you want to print: "))
for r in range(r):
    print("Hello World!")

#Q2. Print natural numbers from 1 to n.
r = int(input("How many numbers do you want to print: "))
for i in range(r+1):
    print(i)

#Q3. Reverse for loop — print n down to 1.
for i in range(r,0,-1):
    print(i)

#Q4. Print the multiplication table of a number.
for i in range(1,11,1):
    print(f"{r} x {i} = {r*i}")

#Q4. Sum of first n natural numbers.
for i in range(r+1):
    r = r + i

print(r)

# Q6. Factorial of a number.
f = 1
for i in range(r+1):
    f = f * i
print(f)

# Q7. Print sum of all even and odd numbers in a range separately.
o = int(input("Tell the End Number: "))
even=0
odd=0
for s in range(1,o+1,1):
    if s % 2 ==0:
        even = even + s
    else:
        odd = odd + s

print(f"Odd Number Sum - {odd}")
print(f"Even Number Sum - {even}")

# Q8. Print all factors of a number.

f = int(input("Enter the Number for Factors: "))
for i in range(1,f+1):
    if f % i == 0:
        print(i)

# Q9. Check if a number is perfect (sum of factors = the number itself).
factorsum = 0
for i in range(1, f):
    if f % i == 0:
        factorsum = factorsum + i

if factorsum == f:
    print(f"Sum of all factor sum is equal to the given Number {factorsum} = {f}")
else:
    print(f"Sum of all factor sum is NOT equal to the given Number {factorsum} != {f}")

# Q10. Check if a number is prime.
PS = 0
P = int(input("To check Prime Number : "))
for prime in range(1, P+1):
    if P % prime ==0:
        PS = PS + prime
if PS == P+1:
    print(f"{P} is a Prime Number")
else:
    print(f"{P} is Not a Prime Number")
'''
## using Counting function---
Alternate way to do the same problem is ====
PS = 0
P = int(input("To check Prime Number : "))
for prime in range(1, P+1):
    if P % prime ==0:
        PS = PS + 1
if PS == 2:
    print(f"{P} is a Prime Number")
else:
    print(f"{P} is Not a Prime Number")
'''

# Q11. Reverse a string without using built-in functions.
#print(a[::-1]) it is using built in funtion
rev =""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]
print(rev)

#Q12. Check if a string is a palindrome.
rev =""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]
if rev==a:
    print("Palindrome!")
else:
    print("Not a Palindrome!")

# Q13. Count letters, digits, and special symbols in a string.
spec = "asdf234*&%$asdhj213*^"
digit = 0
spechar = 0
char = 0
for i in spec:
    if i.isdigit():
        digit = digit + 1
    elif i.isalpha():
        char = char + 1
    else:
        spechar = spechar + 1
print(f"The Number is in String is {digit}")
print(f"The Alphabets in the string is {char}")
print(f"The Special Signs in the string is {spechar}")

### While Loop-
'''
The while loop keeps running as long as a condition is True. You use it when you don't know how many times you'll need to repeat.

count = 1
while count <= 5:
    print(count)
    count += 1

# Output: 1  2  3  4  5
'''
# Q1. Separate each digit of a number and print on a new line.
# Q2. Accept a number and print its reverse.

dig = int(input("Enter the number- "))
rev = 0
copy = dig
while dig > 0:
    rev = rev * 10 + dig%10
    dig = dig // 10

print(rev)

# Q3. Check if a number is palindromic (equal to its reverse).
if rev == copy:
    print("Palindrome!")
else:
    print("Not a Palindrome!")