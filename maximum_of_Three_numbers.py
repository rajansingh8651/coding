num1=int(input("Enter your first number : "))
num2=int(input("Enter your second number : "))
num3=int(input("Enter your third number : "))
if num1 > num2 and num1 > num3:
    print("Number one is greater")
elif num2 > num1 and num2 > num3:
    print("Number two is greater")
else:
    print("Number three is greater")