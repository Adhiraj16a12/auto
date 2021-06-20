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

#You can use the below text to check the output
#Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability. With its notable use of significant whitespace.Used for back end development, software development, data science and writing system scripts among other things.