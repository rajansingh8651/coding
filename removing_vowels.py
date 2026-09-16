# user_sentence=input("Enter your sentence here: ")
# vowels="aeiouAEIOU"
# for i in user_sentence:
#     if i in vowels:
#         user_sentence=user_sentence.replace(i,"")
# print(user_sentence)

def remove_vowels(user_sentence):
    vowels="aeiouAEIOU"
    for i in user_sentence:
        if i in vowels:
            user_sentence=user_sentence.replace(i,"")
    return user_sentence
print(remove_vowels("Hello, how are you?"))