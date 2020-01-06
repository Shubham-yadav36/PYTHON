def is_palin(word):
    if word == word[::-1]:
        return "Yes"
    else:
        return "no"


name = input("enter your name : ")
print(is_palin(name))
