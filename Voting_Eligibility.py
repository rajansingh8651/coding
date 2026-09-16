user_age = int(input("Enter your age please : "))

if user_age >= 18:
    print("You are eligible for the vote")
elif user_age <= 12:
    print("Ohh you are a child")
else:
    print("You are a teenager")
