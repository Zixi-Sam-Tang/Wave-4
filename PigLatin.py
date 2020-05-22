def piglatin(word):
    temp = ""
    vowels = ["a", "e", "i", "o", "u", "y"]
    if word[0] not in vowels:
        for i in range(1, len(word)):
            if word[i] in vowels:
                temp = word[i:len(word)] + word[0:i] + "ay"
                break
    else:
        temp = word + "way"
    return temp
word = str(input("Input word: "))
print(piglatin(word))