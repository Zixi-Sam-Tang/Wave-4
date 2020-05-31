def piglatin(word):
    for j in word:
        temp = ""
        vowels = ["a", "e", "i", "o", "u", "y"]
        if j[0] not in vowels or j[0] == "y":
            for i in range(1, len(j)):
                if j[i] in vowels:
                    temp = j[i:len(j)] + j[0:i] + "ay"
                    break
        else:
            temp = j + "way"
        print(temp, end = " ")
word = str(input("Input word: ")).split(" ")
piglatin(word)