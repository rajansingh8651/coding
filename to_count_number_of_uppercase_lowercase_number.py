user_sentence=input("Enter your sentence here : ")
uppercase_count=0
lowercase_count=0
for i in user_sentence:
    if i.isupper():
        uppercase_count=uppercase_count+1
    elif i.islower():
        lowercase_count=lowercase_count+1
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)