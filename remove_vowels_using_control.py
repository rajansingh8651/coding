def rem_vowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in string.lower():
        if x in vowels:
            continue 
        string = x
        print(string,end="")
string = "i am studying in vignan"
rem_vowel(string)