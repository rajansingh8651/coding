i = 1
sum = 0
n = int(input("Enter how many numbers you have = "))
while i<=n:
    a = int(input(f"Enter {i} Number = "))
    sum += a
    i += 1
print(f"Here is the average of your number = {sum/n}")