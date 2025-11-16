letter = input("Enter a letter: ").lower()
if not letter.isalpha() or len(letter) != 1:
        print("Invalid input")

elif letter in "aeiou":
        print("Vowel")
else:
    print("Consonant")
