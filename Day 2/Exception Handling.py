#Exception Handling

'''
Errors vs Exceptions
❌ Errors (unfixable)
SyntaxError — wrong syntax
IndentationError — bad spacing
TabError — mixing tabs/spaces

✅ Exceptions (handleable!)
ZeroDivisionError
TypeError
ValueError
FileNotFoundError
'''

# try - Wrap the risky code
try:
    result = 10 / 0

# except - Handle the exception
except ZeroDivisionError:
    print("Can't divide by zero!")

#else - Runs only if no exception occurred
else:
    print("Success:", result)

# finally - Always runs — good for cleanup
finally:
    print("This always runs.")


# Prep
a = int(input("Number 1 is - "))
b = int(input("number 2 is - "))
result = 0
try:
    result = a/b
except Exception as err:
    print(f"Error has ourrced in {err}")
else:
    print("No Errors so far!")
finally:
    print(f"Your Result is {result}")

# Raise
age = int(input("What's your age :- "))
if age < 18:
    raise ValueError("You're Not Elegible! ")

print("Your Elegible")
