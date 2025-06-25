# A file contains a word "Donkey" multiple times you need to write a program which replaces this word with ###### by updating the same file

word = "Donkey"

with open("problem4.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("problem4.txt", "w") as f:
    f.write(contentNew)