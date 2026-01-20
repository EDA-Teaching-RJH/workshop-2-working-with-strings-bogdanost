def age_confirm():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are an adult")
    if 0<=age<18:
        print("You are a child")
age_confirm()