import string
user_sentence = input("Enter your sentence here: ")
for char in user_sentence:
    if char in string.punctuation:
        user_sentence = user_sentence.replace(char, "")
print(user_sentence)