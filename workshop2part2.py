import random
number = random.randint(1,10)
print(number)

def check(number):
    user = int(input("Enter your number: "))
    if user == number:
        print("You guessed right")
    elif user > number:
        print("Too high")
    else:
        print("Too low")
check(number)