user = input("Enter text to compress: ")
currentLetter = ""
count = 0

print("Compression: ")
for char in user:
    if currentLetter == "":
        currentLetter = char
        count = 1
    else:
        if char == currentLetter:
            count += 1
       
        else:
            print(currentLetter, count, end = " ")
            currentLetter = char
            count = 1
print(currentLetter, count, end = " ")

