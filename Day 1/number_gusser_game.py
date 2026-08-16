import random
print('''Welcome to the "Guess The Number Game!" ''')

random_num = input("Give the number: ")

if random_num.isdigit():
    random_num = int(random_num)
    if random_num <= 0 :
        print("Plz. Enter a number larger than 0")
        quit()
else:
    print("Please write the number next time!!")
    quit()

max_number = random.randint(0, random_num)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please write the number next time!!")
        continue

    if user_guess == max_number:
        print(f"You Got it!")
        break
    elif max_number > user_guess:
            print("Number is Higher")
    else:
        print("Number is Lower")

print(f"The total number of guesses", guesses)