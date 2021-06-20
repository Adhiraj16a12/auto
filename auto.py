print("Welcome to Sadana's Automated Study Helper!")
print("")
print("This automation will help you memorize paragraphs by splitting the")
print("sentences into small bits")
print("")
print("Enter the text you want to learn: ")
text = input()

print("")
print("")
textSplit = text.split(".")

print("Your input has been simplified! Here you go!!")
for txt in range(len(textSplit)):
    print("")
    print(" " + textSplit[txt])

