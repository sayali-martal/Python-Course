# Replace the vowel in a string
# abcd = g
# phrase = This is a dog


def translate(phrase):
    translate = ""
    for letter in phrase:
        if letter in "aeiouAEIOU":
            if letter.isupper():
                translate = translate + "G"
            else:
                translate = translate + "g"
        else:
            translate = translate + letter

    return translate


print(translate(input("enter a string:")))
