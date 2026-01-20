score = int(input("Enter your score (0-100): "))

def grade(score):
    if 90 <= score <= 100:
        grade = "Your garde is A"
    elif 80 <=score<= 89:
        grade = "Your garde is B"
    elif 70 <=score<= 79:
        grade = "Your garde is C"
    elif 60 <=score<= 69:
        grade = "Your garde is D"
    elif score > 100 or score < 0:
        grade = "Incorrect value"
    else:
        grade = "Your garde is E"
    print(grade)
grade(score)