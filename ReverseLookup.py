dictionary = {'computer science' : 'fun', 'coding' : 'fun', 'food' : 'delicious', 'video games' : 'fun to play with friends', 'procrastination' : 'I do it too!'}
value = input("Input the value: ")
keyFound = False
for i in dictionary:
    if dictionary[i] ==  value:
        print(i)
        keyFound = True
if not keyFound:
    print("No keys found.")