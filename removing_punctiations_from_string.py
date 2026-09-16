import string
user_string = input("Enter string: ")
print(user_string.translate(str.maketrans('', '', string.punctuation)))
