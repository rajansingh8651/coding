string = input ("Enter your string here :")
lower=0
upper=0
for i in string:
    if (i.islower()):
        lower=lower+1
    elif (i.isupper()):
        upper=upper+1
print("The number of upper case is : ",upper)
print("The number of lower case is ",lower)