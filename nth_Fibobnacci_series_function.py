def fibonacci_number(number):
    if number <=0:
        print(str(number)+" Invalid number")
    elif number==1:
        return 0
    elif number==2:
        return 1
    else:
        return fibonacci_number(number-1)+fibonacci_number(number-2)
print(fibonacci_number(8))