def factorial(number):
    if number==1:
        return number
    else:
        return number*(number-1)
num=int(input("Enter your number : "))
if num==0:
    print("1")
elif num<0:
    print("Negavtive number factorial doesnot exist")
else:
    print("Factorial of ",num," is = ",factorial(num))